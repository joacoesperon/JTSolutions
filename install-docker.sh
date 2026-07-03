#!/usr/bin/env bash
# Instala Docker Engine en Ubuntu 24.04 (WSL2) y lo deja listo para usar sin sudo.
# Uso:  sudo bash install-docker.sh
set -e

echo "==> [1/6] Dependencias base..."
apt-get update -qq
apt-get install -y -qq ca-certificates curl >/dev/null

echo "==> [2/6] Llave GPG oficial de Docker..."
install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
chmod a+r /etc/apt/keyrings/docker.asc

echo "==> [3/6] Repositorio de Docker..."
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" \
  > /etc/apt/sources.list.d/docker.list

echo "==> [4/6] Instalando Docker Engine (puede tardar)..."
apt-get update -qq
apt-get install -y -qq docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin >/dev/null

echo "==> [5/6] Arrancando el daemon..."
# WSL2: systemd si está disponible, si no dockerd en background
if command -v systemctl >/dev/null 2>&1 && systemctl is-system-running >/dev/null 2>&1; then
  systemctl enable --now docker || service docker start
else
  service docker start || (dockerd >/var/log/dockerd.log 2>&1 &)
fi
sleep 3

echo "==> [6/6] Permitir usar docker sin sudo en esta sesión..."
# ${SUDO_USER} es tu usuario real (jesperon) aunque el script corra como root
REAL_USER="${SUDO_USER:-$USER}"
usermod -aG docker "$REAL_USER" || true
# Truco WSL: dar acceso inmediato al socket sin cerrar la terminal
chmod 666 /var/run/docker.sock 2>/dev/null || true

echo ""
echo "==> Verificación:"
docker --version
echo ""
echo "======================================================"
echo " LISTO. Docker instalado y corriendo."
echo " Volvé a la conversación con Claude y avisá que terminó."
echo "======================================================"
