# PLANTILLA — Tu MasKota Chula (web en GoHighLevel, calcada de gentlecan.es)

Documento maestro. **Parte 1** = lo ya construido (estado actual). **Parte 2** = lo que
falta, con valores exactos extraídos del CSS real de gentlecan (adaptados a nuestra marca).

**Colores de esta página:** naranja `#fcb423` (botones/acentos) · verde `#7CBA3F`
(secciones color) · crema `#FFF7E5` (secciones claras) · texto oscuro `#252525` · párrafos
`#000000` · blanco `#FFFFFF`.
**Fuentes:** DM Sans (todo) · DM Serif Display (títulos hero/CTA/ubicación).
**Links pendientes de conectar al final:** `#reservar` → url del calendario · menú → css
selectors de las secciones · Instagram · Google Maps · reseñas de Google.

---
---

# PARTE 1 — YA CONSTRUIDO (estado actual)

## SECCIÓN header

**general settings**
- element name: `header` · sticky: **no** · allow rows to take entire width: **no** · width: **full**

**style settings**
- margen: 0 (desktop y móvil)
- padding desktop: arriba 15px · derecha 40px · abajo 15px · izquierda 40px
- padding móvil: arriba 12px · derecha 20px · abajo 12px · izquierda 20px
- border none · shadow none · visibility todos · custom class `header`
- background: `#fcb423`

### elemento navigation menu → `nav-menu`
- **menu items:** Inicio → css selector de `hero` · Nosotros → css selector de `nosotros` ·
  Servicios → css selector de `servicios` · Opiniones → css selector de `testimonios` ·
  Reservar → url del calendario (por ahora `#reservar`)
- **acción del logo:** volver arriba (css selector de `hero`)
- **logo:** alto 50px desktop · 40px móvil
- **tipografía:** DM Sans · 16px · weight 500 · line height 1.5
- **estilo:** margen 0 · padding 0 (desktop y móvil) · menu item alignment: right ·
  menu item spacing: 24px desktop / 16px móvil · align: right · container size: 1200px
- **color texto:** `#252525` · **hover:** `#FFFFFF` · móvil: hamburguesa

---

## SECCIÓN hero

**general settings**
- element name: `hero` · sticky: **no** · allow rows to take entire width: **no** · width: **full**
- background: **imagen** + background image opacity: **half fade**

**style settings**
- margen: 0 (desktop y móvil)
- padding desktop: arriba 160px · derecha 40px · abajo 160px · izquierda 40px
- padding móvil: arriba 100px · derecha 20px · abajo 100px · izquierda 20px
- border none · shadow none · visibility todos · custom class `hero`

**fila `hero-fila`**: align center · width 100% · margen 0 · padding 0 (d y m)
**columna `hero-col`**: Content Alignment **Vertical** · Content Spacing **Center** ·
Content Position **Center** · Use Same layout for Mobile **sí** · margen 0 · padding 0

### 1) `hero-eyebrow` — Sub-Headline
- contenido: `LA FÁBRICA DE PELUCHES`
- config contenido: DM Sans · 15px · `#FFFFFF` · negrita/itálica/subrayado/tachado off
- tipografía: content font · 15px desktop / 13px móvil · w500 · opacity 100% · lh 1.4 ·
  transform uppercase · letter spacing 3px
- color `#FFFFFF` · margen: abajo 16px (resto 0, d y m) · padding 0 · align center ·
  border/shadow none · custom class `hero-eyebrow`

### 2) `hero-titulo` — Headline → H1
- contenido: `Peluquería Canina en Madrid`
- config contenido: DM Serif Display · 64px · `#FFFFFF` · todo off
- tipografía: custom font DM Serif Display · 64px desktop / 40px móvil · w400 ·
  opacity 100% · lh 1.1 · transform none · ls 0
- color `#FFFFFF` · margen: abajo 24px (resto 0) · padding 0 · align center · custom class `hero-titulo`

### 3) `hero-texto` — Paragraph
- contenido: `Una **experiencia de lujo para perros**, en Tu MasKota Chula encontrarás los
  **mejores servicios de baño, peluquería, corte y mucho más;** para mimar a los
  consentidos de la familia.` (negrita ON en las frases marcadas)
- tipografía: content font · 20px desktop / 16px móvil · w400 · opacity 100% · lh 1.6 ·
  transform none · ls 0
- color `#FFFFFF` · margen: abajo 36px (resto 0) · padding 0 · align center ·
  container size 650px · custom class `hero-texto`

### 4) `hero-boton` — Button
- contenido: `Reserva ya` · action: link → `#reservar`
- tipografía: DM Sans · 17px desktop / 16px móvil · w600
- color texto `#252525` · fondo `#fcb423`
- border radius 8px · align center · padding botón 16px 40px desktop / 14px 32px móvil · margen 0
- ⚠️ opcional para igualar 100% a gentlecan y al resto de botones: radius **10px**,
  padding **20px 30px**, 18px w400

---

## SECCIÓN nosotros

**general settings**
- element name: `nosotros` · sticky no · allow rows: no · width full · background `#FFF7E5`

**style settings**
- margen 0 · padding desktop: arriba 50px · derecha 20px · abajo 80px · izquierda 20px ·
  padding móvil: arriba 50px · derecha 20px · abajo 50px · izquierda 20px
- border/shadow none · custom class `nosotros`

### filas
- `nosotros-bloque1`: align center · width 100% · margen abajo 50px desktop / 40px móvil
  (resto 0) · padding 0 · 2 columnas 50/50 (izq texto, der foto)
- `nosotros-bloque2`: margen abajo 120px desktop / 50px móvil · padding 0 · 2 col 50/50 (texto/texto)
- `nosotros-bloque3`: margen 0 · padding 0 · 2 col 50/50 (foto/texto)
- `nosotros-galeria`: margen arriba 50px desktop / 40px móvil (resto 0) · padding 0 · 1 columna

### columnas
Todas: Content Alignment **Vertical** · Content Spacing **Center** · Use Same layout for
Mobile **sí**. Content Position: **Default** en las de texto, **Center** en las de foto.

- `bloque1-txt-col`: padding desktop arriba 40 / derecha 60 / abajo 0 / izquierda 80 ·
  móvil todo 0 · margen móvil abajo 40px
- `bloque1-img-col`: padding 0 (d y m)
- `bloque2-txt-col-izq`: padding desktop arriba 20 / derecha 60 / abajo 0 / izquierda 80 ·
  móvil 0 · margen móvil abajo 20px
- `bloque2-txt-col-der`: padding 0 (d y m)
- `bloque3-img-col`: padding desktop derecha 60 (resto 0) · móvil 0 · margen móvil abajo 40px
- `bloque3-txt-col`: padding desktop arriba 40 / izquierda 20 (resto 0) · móvil 0

### elementos de texto (config idéntica en los 3 bloques)

**`bloqueN-titulo`** — Sub-Headline → H3
- tipografía: content font · 16px (d y m) · w400 · lh default · **uppercase** · ls 2px
- color `#fcb423` · margen abajo 15px · padding 0 · align left

**`bloqueN-subtitulo`** — Headline → H2
- tipografía: content font DM Sans · 30px (d y m) · **w700** · lh 1.13 · transform none
- color `#252525` · margen abajo: fila1 15px / fila2 0 / fila3 20px (móvil fila3: 0) ·
  padding 0 · align left

**`bloqueN-texto`** — Paragraph
- tipografía: content font · 20px (d y m) · w400 · lh 1.2 · transform none
- color `#000000` · negritas ON en frases marcadas · margen 0 · padding 0 · align left
- solo fila 3: container size 380px

### elementos imagen — `bloque1-img` / `bloque3-img`
- size: width **100%** (height auto) · border radius 16px · align center · margen/padding 0
- las fotos con el mismo aspect ratio (4:3) para que queden parejas

### contenido
**Bloque 1** (Sobre nosotros)
- titulo: `Sobre nosotros`
- subtitulo: `Sabemos lo que tu mascota significa para tu familia`
- texto: `Por eso hemos creado un lugar único, **en el que los dueños puedan confiar,** y
  en el que tu perro no solo derroche belleza y estilo, sino que **sienta todo el cariño y
  el amor que se merece.**`

**Bloque 2** (Nuestra filosofía) — izq: titulo+subtitulo · der: texto
- titulo: `Nuestra filosofía`
- subtitulo: `Cada perro es único y especial para nosotros y ¡ellos lo notan!`
- texto: `En función de su raza, tipo de pelaje y preferencias de sus dueños **orientamos
  nuestros trabajos para conseguir siempre un resultado óptimo, tanto por sus necesidades
  higiénicas como estéticas.** Gracias a nuestras herramientas y técnicas especializadas,
  **tenemos el don de satisfacer hasta a los clientes más exigentes,** ya sea con un
  elegante corte a tijera, un meticuloso Hand-Stripping o un atrevido corte creativo.`

**Bloque 3** (Nuestro equipo)
- titulo: `Nuestro equipo`
- subtitulo: `Hemos de decir, ¡qué no hay corte que se nos resista!`
- texto: `En Tu MasKota Chula **contamos con un equipo profesional altamente cualificado y
  en constante formación.** Nos especializamos en las diferentes razas y pelajes, siendo
  **expertos en Caniche, Shih Tzu, Bichón Maltés, Yorkshire, Schnauzer, West Highland
  Terrier** y muchas más. ¿Nuestro objetivo? No solo realzar la belleza de cada perro,
  sino también **garantizar su comodidad y bienestar durante el proceso.**`

### galería — columna única (CA Vertical · CS Center · CP Default · same mobile sí · todo 0)
Elemento **Custom Code** → `galeria-code`. Estado actual: 9 fotos cargadas (falta la 10ª,
se agrega con otra línea `<img>`). El código con `!important` para que GHL no pise los
anchos: 5 por pantalla desktop, 2 en móvil, lightbox al clic. (El código completo está en
la página; plantilla del código con URLs a reemplazar por cliente.)

---
---

# PARTE 2 — POR CONSTRUIR (valores exactos de gentlecan)

> Referencia gentlecan → nuestro: su naranja `#FF9C0D` → `#fcb423` · su verde `#00544D` →
> `#7CBA3F` · su crema `#FFF7E5` → igual.
> **Botón estándar de aquí en adelante (exacto de gentlecan):** fondo `#fcb423` · texto
> `#252525` · DM Sans 18px w400 · border radius 10px · padding botón 20px 30px · hover un
> poco más claro.

## SECCIÓN cta  (va después de nosotros)

**general settings**
- element name: `cta` · sticky no · allow rows: no · width full
- background: color `#7CBA3F` (+ textura transparente opcional, ver "TEXTURA" al final)

**style settings**
- margen 0 · padding desktop: arriba 40px · derecha 20px · abajo 40px · izquierda 20px ·
  padding móvil: igual (40/20/40/20)
- border/shadow none · custom class `cta`

**fila `cta-fila`**: align center · width 100% · margen/padding 0
**columna `cta-col`**: CA Vertical · CS Center · CP Center · same mobile sí · margen/padding 0

### 1) `cta-titulo` — Headline → H2
- contenido: `Es por eso por lo que, para muchos,` (salto de línea) `somos la mejor
  peluquería canina de Madrid.`
- tipografía: custom font DM Serif Display · **45px** desktop / **35px** móvil · w400 ·
  lh 1.11 desktop / 1.25 móvil · transform none · ls 0
- color `#FFFFFF` · margen abajo 50px (resto 0) · padding 0 · align center ·
  container size 960px · custom class `cta-titulo`

### 2) `cta-boton` — Button (botón estándar)
- contenido: `Reserva ya` · link `#reservar`
- DM Sans 18px w400 · texto `#252525` · fondo `#fcb423` · radius 10px · padding 20px 30px ·
  align center · margen 0 (móvil: abajo 20px)

---

## SECCIÓN servicios

**general settings**
- element name: `servicios` · sticky no · allow rows: no · width full · background `#FFF7E5`

**style settings**
- margen 0 · padding desktop: arriba 70px · derecha 20px · abajo 80px · izquierda 20px ·
  móvil: 50/20/50/20
- border/shadow none · custom class `servicios` (css selector → item "Servicios" del menú)

**fila `servicios-titulos`**: align center · width 100% · margen abajo 40px (d y m) ·
padding 0 · 1 columna (CA Vertical · CS Center · CP Default · same sí · todo 0)

### 1) `servicios-eyebrow` — Sub-Headline → H3
- contenido: `Técnicas y servicios de peluquería`
- tipografía: content font · 16px (d y m) · w400 · **uppercase** · ls 2px
- color `#fcb423` · margen abajo 10px · padding 0 · align **center**

### 2) `servicios-titulo` — Headline → H2
- contenido: `Cortes y baños para perros`
- tipografía: content font DM Sans · **35px** desktop / 30px móvil · **w700** · lh default
- color `#252525` · margen 0 · padding 0 · align **center**

**filas de tarjetas**: `servicios-fila1` (4 columnas 25%) · `servicios-fila2` (4 columnas
25%) · `servicios-fila3` (1 columna, tarjeta centrada o ancho 25%). align center ·
width 100% · margen abajo 0 · padding 0.

### columnas-tarjeta (las 9 IDÉNTICAS) → `tarjeta-1` … `tarjeta-9`
- Column Layout: CA Vertical · CS Center · CP Default · same mobile sí
- background: **`#FFFFFF`**
- style: margen 10px en los 4 lados (d y m) · padding desktop/móvil: arriba 30px ·
  derecha 15px · abajo 30px · izquierda 15px
- border: radius **5px** (sin borde) · shadow none · custom class `tarjeta-N`

### elementos de cada tarjeta (todos align center)
1. **`tarjetaN-icono`** — Image: pictograma del servicio · width **125px** · align center ·
   margen abajo 0 · padding 0
2. **`tarjetaN-nombre`** — Headline → H3: DM Sans · **25px** (d y m) · **w700** ·
   color `#252525` · margen abajo 20px · padding 0
3. **`tarjetaN-texto`** — Paragraph: DM Sans · **16px** (d y m) · w400 · **lh 1.2** ·
   color `#000000` · margen abajo 30px · padding 0
4. **`tarjetaN-foto`** — Image: foto del servicio · width **180px** ·
   border radius **50%** (redonda) · align center · margen/padding 0

### contenido de las 9 tarjetas
1. **Corte Comercial** — `El corte más habitual, práctico y funcional. Incluye baño
   completo, cosmética profesional, corte de uñas, limpieza de oídos y vaciado de glándulas.`
2. **Corte a Tijera** — `La técnica de precisión por excelencia: un corte íntegro a
   tijera, con un acabado natural y estilizado.`
3. **Hand-Stripping** — `Retiramos de forma manual el pelo maduro dejando crecer una capa
   nueva. Ideal para razas de pelo duro.`
4. **Corte Creativo** — `¡Solo para los más atrevidos! Transformamos un estilo comercial
   en un look original y artístico.`
5. **Arreglo Cachorro** — `Su primera visita a la peluquería, convertida en una
   experiencia tranquila y gratificante.`
6. **Corte Deslanado** — `Eliminamos el exceso de pelo muerto o muda en perros de doble
   capa, para un manto sano y sin enredos.`
7. **Baño pelo corto** — `Baños con productos de alta calidad y masajes relajantes que
   dejan el pelaje brillante.`
8. **Mantos Largos** — `Baños de hidratación para mantos secos, dañados o muy largos que
   requieren un cuidado especial.`
9. **Baño y arreglo** — `Ningún perro sale sin su arreglo higiénico, un retoque del largo
   y una buena ración de mimos.`

**fila `servicios-boton`** (cierre): 1 columna centrada · margen arriba 20px · elemento
Button `Reserva ya` → `#reservar` (botón estándar, align center).

---

## SECCIÓN testimonios

**general settings**
- element name: `testimonios` · sticky no · allow rows: no · width full · background `#FFF7E5`

**style settings**
- margen 0 · padding desktop: arriba 70px · derecha 20px · abajo 40px · izquierda 20px ·
  móvil 50/20/30/20
- border/shadow none · custom class `testimonios` (css selector → item "Opiniones")

**fila `testimonios-titulos`**: 1 columna (CA Vertical · CS Center · CP Default · same sí ·
todo 0) · margen abajo 0 · padding 0

### 1) `testi-eyebrow` — Sub-Headline → H3
- contenido: `Testimonios` · content font · 16px · w400 · **uppercase** · ls 2px ·
  color `#fcb423` · align **center** · margen abajo 15px

### 2) `testi-titulo` — Headline → H2
- contenido: `Comentarios reales de nuestros clientes`
- DM Sans · **35px** desktop / **30px** móvil · **w700** · color `#252525` · align center ·
  container size **500px** · margen abajo 40px

**fila `testimonios-cards`**: 3 columnas 33/33/33 · align center · margen abajo 30px · padding 0

### columnas-reseña (las 3 IDÉNTICAS) → `resena-1` / `resena-2` / `resena-3`
- CA Vertical · CS Center · CP Default · same mobile sí
- style: margen desktop: derecha 10px · izquierda 10px (resto 0) · margen móvil: derecha
  20px · izquierda 20px · abajo 20px · padding 30px en los 4 lados (d y m)
- border: **1px sólido `#CCCCCC`** · radius **5px** · shadow none · background blanco o
  transparente · custom class `resena-N`

### elementos de cada reseña (align left)
1. **`resenaN-texto`** — Paragraph: la reseña entre comillas “...” · DM Sans · **18px** ·
   w400 · **lh 1.33** · color `#252525` · margen abajo 20px
2. **`resenaN-nombre`** — Sub-Headline: DM Sans · **16px** · w400 · color `#252525` ·
   margen abajo 6px
3. **`resenaN-estrellas`** — Paragraph: `★★★★★` · 14px · color `#fcb423` · ls 3px · margen 0

### contenido (reseñas para la demo)
1. `“El trato que le dieron a Toby fue excepcional. Salió feliz y con un corte perfecto.
   Sin duda, la mejor peluquería canina a la que hemos ido.”` — `Laura G. · dueña de Toby (Caniche)`
2. `“Luna es muy miedosa con el agua, pero supieron calmarla desde el primer minuto. Se
   nota el mimo con el que trabajan. Muy recomendable.”` — `Carlos R. · dueño de Luna (Yorkshire)`
3. `“Son verdaderos especialistas. El arreglo de Max quedó impecable, respetando el
   estándar de su raza. Los recomiendo al 100%.”` — `Elena M. · dueña de Max (Schnauzer)`

**fila `testimonios-badge`**: 1 columna centrada · margen abajo 30px · elemento **Image**
`badge-google` (imagen del badge de Google: logo + 5 estrellas + nota) · align center ·
**add link → url de las reseñas de Google del negocio** (abrir en pestaña nueva).

---

## SECCIÓN ubicacion

En gentlecan el verde va **en la columna de texto**, no en la sección (la sección tiene
márgenes laterales de 20px y fondo claro — el bloque verde queda "flotando").

**general settings**
- element name: `ubicacion` · sticky no · allow rows: no · width full · background `#FFF7E5`

**style settings**
- margen 0 · padding desktop: arriba 0 · derecha 20px · abajo 60px · izquierda 20px ·
  móvil: arriba 40px · derecha 0 · abajo 40px · izquierda 0
- border/shadow none · custom class `ubicacion`

**fila `ubicacion-fila`**: 2 columnas 50/50 · align center · margen/padding 0

### columna izquierda `ubicacion-txt-col`
- CA Vertical · CS Center · CP Center · same mobile no
- **background: color `#7CBA3F`** (+ textura opcional)
- style: margen 0 · padding desktop: arriba 100px · derecha 40px · abajo 100px ·
  izquierda 100px · padding móvil: 20px los 4 lados
- border/shadow none · custom class `ubicacion-txt-col`

**elementos (align left):**
1. **`ubi-eyebrow`** — Sub-Headline → H3: `Peluquería canina en Madrid` · content font ·
   16px · w400 · **uppercase** · ls 2px · color `#fcb423` · margen abajo 15px
2. **`ubi-titulo`** — Headline → H2: `Visítanos en nuestro espacio exclusivo` ·
   custom font **DM Serif Display** · **45px** desktop / 35px móvil · w400 ·
   color `#FFFFFF` · container size **450px** · margen abajo 20px
3. **`ubi-texto1`** — Paragraph: `Estamos en pleno corazón de Madrid, por lo que ante la
   pregunta ¿hay alguna peluquería canina cerca de mí?, la respuesta es SÍ, y no una
   cualquiera.` · DM Sans · **16px** · w400 · **lh 1.2** · color `#FFFFFF` ·
   container size **390px** · margen abajo 30px
4. **`ubi-texto2`** — Paragraph: `Del baño más relajante al corte más exclusivo.
   **¡Un espacio único para tu perro!**` · misma config que texto1 · margen abajo 30px
5. **`ubi-boton`** — Button: `Ver ubicación` → **url de Google Maps del negocio** (pestaña
   nueva) · botón estándar (fondo `#fcb423` · radius 10 · padding 20/30 · 18px w400) ·
   texto `#252525` *(gentlecan usa su verde oscuro de texto; si lo querés fiel: `#3F6B1F`)* ·
   align left · margen 0 (móvil abajo 20px)

### columna derecha `ubicacion-img-col`
- CA Vertical · CS Center · CP Center · same mobile no · margen/padding 0
- **elemento Image `ubicacion-img`**: foto de la tienda (fachada o interior) ·
  width **100%** (height auto) · radius 0 · align center · margen/padding 0
- en móvil queda debajo del bloque verde (se apila solo)

---

## SECCIÓN siguenos

**general settings**
- element name: `siguenos` · sticky no · allow rows: no · width full
- background: color `#7CBA3F` (+ textura opcional)

**style settings**
- margen 0 · padding desktop: arriba 20px · derecha 20px · abajo 40px · izquierda 20px ·
  móvil igual
- border/shadow none · custom class `siguenos`

**fila `siguenos-fila`**: 1 columna (CA Vertical · CS Center · CP Center · same sí · todo 0)

**elementos (todos align center):**
1. **`siguenos-icono`** — Image: logo de Instagram (blanco o naranja) · width **50px** ·
   margen abajo 15px
2. **`siguenos-titulo`** — Headline → H2: `¡Síguenos!` · DM Sans · **35px** desktop /
   30px móvil · **w700** · color `#FFFFFF` · margen abajo 15px
3. **`siguenos-handle`** — Sub-Headline: `@tumaskotachula` · DM Sans · **18px** · w400 ·
   color `#fcb423` · add link → perfil de Instagram · margen abajo 20px
4. **`siguenos-boton`** — Button: `Seguir en Instagram` → perfil de Instagram (pestaña
   nueva) · botón estándar · align center · margen 0

---

## SECCIÓN footer

**general settings**
- element name: `footer` · sticky no · allow rows: no · width full
- background: color `#7CBA3F` *(gentlecan usa un degradado verde→verde oscuro; opcional
  con custom class + css: `linear-gradient(270deg,#7CBA3F 0%,#4E7A24 100%)`)*

**style settings**
- margen 0 · padding desktop: arriba 60px · derecha 20px · abajo 20px · izquierda 20px ·
  móvil: arriba 40px · derecha 20px · abajo 20px · izquierda 20px
- border/shadow none · custom class `footer`

**fila `footer-columnas`**: 3 columnas **40% / 30% / 30%** · align center · margen abajo
30px · padding 0. Columnas: CA Vertical · CS Center · CP Default · same mobile no ·
padding desktop 0 (móvil: 20px los 4 lados).

### columna 1 `footer-col-logo`
1. **`footer-logo`** — Image: logo versión clara/blanca · width **270px** · align left ·
   margen abajo 10px
2. **`footer-tagline`** — Paragraph: `Peluquería canina en Madrid` · DM Sans · **21px** ·
   w400 · lh 1.24 · color `#FFFFFF` · align left · padding derecha 60px · margen abajo 10px
3. **`footer-social`** — iconos Instagram + Facebook · tamaño **24px** · color `#fcb423` ·
   sin fondo · align left

### columna 2 `footer-col-info`
1. **`footer-info-titulo`** — Sub-Headline → H3: `Información` · DM Sans · **20px** ·
   w400 · color `#fcb423` · align left · margen abajo 15px
2. **`footer-info-links`** — lista de textos con link (uno debajo del otro, separación
   5px): `Inicio` · `Nosotros` · `Servicios` · `Opiniones` · `Reservar` → mismos destinos
   que el menú · DM Sans · 16px · w400 · color `#FFFFFF` (hover blanco 80%)

### columna 3 `footer-col-pelu`
1. **`footer-pelu-titulo`** — Sub-Headline → H3: `Peluquería Canina` · misma config que
   `footer-info-titulo`
2. **`footer-pelu-texto`** — Paragraph (con saltos de línea): `Reserva tu cita` (con link
   a `#reservar`) ⏎ `–` ⏎ `Lunes a viernes` ⏎ `De 10:00h a 19:00h` ⏎ `Sábados consultar` ⏎
   `Calle Principal 123, Madrid` ⏎ `+34 900 123 456` · DM Sans · **16px** · w400 ·
   **lh 1.87** · color `#FFFFFF` · align left

### barra inferior
**fila `footer-divider`**: 1 columna · elemento **Divider**: color `#fcb423` · alto 1px ·
width 100% · margen arriba 10px / abajo 20px
**fila `footer-legal`**: 2 columnas 50/50 · margen/padding 0
1. **`footer-copy`** — Paragraph: `© 2026 Tu MasKota Chula. Todos los derechos reservados.` ·
   DM Sans · **13px** · w400 · color `#FFFFFF` · align left (móvil center)
2. **`footer-legales`** — Paragraph: `Política de Privacidad · Aviso Legal` · 13px ·
   color `#FFFFFF` · align right (móvil center)

---

## BOTONES FLOTANTES (custom code, una vez en la página)

Elemento **Custom Code** → `flotantes-code` (en cualquier sección; queda fijo):

```html
<div class="flotantes">
  <a class="f-tel"  href="tel:+34900123456" aria-label="Llamar">📞</a>
  <a class="f-wa"   href="https://wa.me/34900123456" target="_blank" aria-label="WhatsApp">💬</a>
  <a class="f-mail" href="mailto:hola@tumaskotachula.es" aria-label="Email">✉️</a>
</div>
<style>
.flotantes{position:fixed;right:24px;bottom:24px;display:flex;flex-direction:column;gap:12px;z-index:99999;}
.flotantes a{width:56px;height:56px;border-radius:50%;display:flex;align-items:center;justify-content:center;
  color:#fff;box-shadow:0 4px 12px rgba(0,0,0,.25);font-size:24px;text-decoration:none;}
.f-tel{background:#7CBA3F;} .f-wa{background:#25D366;} .f-mail{background:#fcb423;}
</style>
```
(Cambiar teléfono/WhatsApp/email por los del cliente. Los emojis se pueden reemplazar por
SVGs cuando queramos afinar.)

---

## TEXTURA VERDE (opcional — lo que hace gentlecan)

gentlecan usa una **imagen de textura** sobre el color (la misma en verde y en azul según
la página). Para replicarlo escalable a cualquier color de cliente:
1. Descargar una textura **PNG transparente** de transparenttextures.com (o patrón SVG con
   color configurable de heropatterns.com).
2. En cada sección/columna verde: background **color** `#7CBA3F` **+ background image** la
   textura PNG (repeat). El color de abajo se ve a través → **un solo archivo sirve para
   todos los colores**.
3. Si el resultado no convence: color liso y listo.

---

## CONEXIONES FINALES (checklist al terminar de armar)
- [ ] Copiar el **css selector** de cada sección (`hero`, `nosotros`, `servicios`,
  `testimonios`) → pegarlos como links de los items del menú y del footer
- [ ] Crear el **calendario** en GHL → reemplazar TODOS los `#reservar` (menú, hero, cta,
  servicios, footer "Reserva tu cita")
- [ ] URL real de **Instagram** (síguenos + footer)
- [ ] URL real de **Google Maps** (ubi-boton)
- [ ] URL de **reseñas de Google** (badge de testimonios)
- [ ] Teléfono/WhatsApp/email reales en botones flotantes
- [ ] 10ª foto de la galería
- [ ] Favicon + título de la página con el nombre del negocio
