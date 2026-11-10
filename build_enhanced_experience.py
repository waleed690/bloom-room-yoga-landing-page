import json
import os

with open('/home/antigravity/assets/images_b64.json') as f:
    b64 = json.load(f)

HERO_B64 = b64['hero']
INSTRUCTOR_B64 = b64['instructor']
RITUAL_B64 = b64['ritual']
TEA_B64 = b64['tea_lounge']
BOWL_B64 = b64['sound_bowl']

artifact_dir = '/home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p/2b05636d-5091-4410-a4e0-8e365c612f9a'

# ==============================================================================
# 1. BUILD STANDALONE ARTIFACT (bloom_room_landing_page.html)
# ==============================================================================
html_artifact = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bloom Room Yoga — 6-Week Spring Renewal Program</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,400;1,600&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');
    
    :root {{
      --font-serif: 'Cormorant Garamond', Georgia, serif;
      --font-sans: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
      --color-terracotta: #C87D55;
      --color-terracotta-dark: #B16943;
      --color-forest: #4A6054;
      --color-forest-dark: #37473E;
      --color-sage: #8E9B82;
      --color-bg: #FAF7F2;
    }}

    body {{
      font-family: var(--font-sans);
      background-color: var(--color-bg);
      color: #1D231F;
      margin: 0;
      padding: 0;
      -webkit-font-smoothing: antialiased;
    }}

    .font-serif-luxury {{
      font-family: var(--font-serif);
    }}

    .serif-italic {{
      font-family: var(--font-serif);
      font-style: italic;
    }}

    /* Sound visualizer animation */
    @keyframes soundBar {{
      0%, 100% {{ height: 4px; }}
      50% {{ height: 22px; }}
    }}
    .sound-active .bar-1 {{ animation: soundBar 1.1s ease-in-out infinite; }}
    .sound-active .bar-2 {{ animation: soundBar 0.8s ease-in-out infinite 0.2s; }}
    .sound-active .bar-3 {{ animation: soundBar 1.4s ease-in-out infinite 0.4s; }}
    .sound-active .bar-4 {{ animation: soundBar 0.9s ease-in-out infinite 0.1s; }}
    .sound-active .bar-5 {{ animation: soundBar 1.2s ease-in-out infinite 0.3s; }}
  </style>
</head>
<body class="bg-[#FAF7F2] text-[#1D231F] antialiased">

  <!-- Top Announcement Bar -->
  <div class="bg-[#37473E] text-[#F4EFEA] text-xs py-2.5 px-4 sticky top-0 z-50 shadow-sm border-b border-white/10">
    <div class="max-w-6xl mx-auto flex flex-wrap items-center justify-between gap-2">
      <div class="flex items-center gap-2">
        <span class="bg-[#C87D55] text-white px-2.5 py-0.5 rounded-full font-semibold tracking-wide text-[11px]">🌱 Spring Cohort 2026</span>
        <span>Starts Monday, April 6 • <strong>Only 6 of 24 mats remain</strong></span>
      </div>
      <div class="flex items-center gap-2 font-mono text-xs">
        <span class="text-stone-300 font-sans">Early-Bird Closes In:</span>
        <span class="bg-black/30 px-2.5 py-0.5 rounded text-[#F8D9C8] font-bold tracking-wider" id="artTimer">04d : 12h : 48m : 30s</span>
      </div>
    </div>
  </div>

  <!-- Header -->
  <header class="bg-[#FAF7F2]/95 backdrop-blur-md border-b border-stone-200 sticky top-9 z-40">
    <div class="max-w-6xl mx-auto px-6 h-20 flex items-center justify-between">
      <div class="flex items-center gap-3">
        <svg class="w-9 h-9 flex-shrink-0" viewBox="0 0 32 32" fill="none">
          <path d="M16 3C16 3 10 9 10 15C10 18.3137 12.6863 21 16 21C19.3137 21 22 18.3137 22 15C22 9 16 3 16 3Z" fill="#C87D55" fill-opacity="0.95"/>
          <path d="M7 11C7 11 3 17 6 21C8.2 24 12 23 14 20C12 18 10 14 7 11Z" fill="#8E9B82"/>
          <path d="M25 11C25 11 29 17 26 21C23.8 24 20 23 18 20C20 18 22 14 25 11Z" fill="#8E9B82"/>
          <path d="M16 21V29M16 29C14 27.5 12 27 10 27M16 29C18 27.5 20 27 22 27" stroke="#4A6054" stroke-width="2" stroke-linecap="round"/>
        </svg>
        <div>
          <span class="font-serif-luxury text-2xl font-bold tracking-widest block leading-none text-stone-900">BLOOM ROOM</span>
          <span class="text-[10px] tracking-widest font-semibold text-[#4A6054] block mt-0.5">YOGA & SANCTUARY • MILL VALLEY</span>
        </div>
      </div>

      <nav class="hidden md:flex items-center gap-7 text-sm font-medium text-stone-600">
        <a href="#art-curriculum" class="hover:text-[#4A6054] transition">The 6 Weeks</a>
        <a href="#art-gallery" class="hover:text-[#4A6054] transition">Sanctuary Gallery</a>
        <a href="#art-mats" class="hover:text-[#4A6054] transition">Select Mat</a>
        <a href="#art-sound" class="hover:text-[#4A6054] transition">Sound Bath</a>
        <a href="#art-quiz" class="hover:text-[#4A6054] transition">Renewal Quiz</a>
        <a href="#art-investment" class="hover:text-[#4A6054] transition">Tuition</a>
      </nav>

      <div class="flex items-center gap-3">
        <button type="button" onclick="artOpenModal()" class="bg-[#C87D55] hover:bg-[#B16943] text-white px-6 py-2.5 rounded-full text-xs font-semibold tracking-wide shadow-md transition transform hover:-translate-y-0.5">
          Reserve Your Mat
        </button>
      </div>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="py-14 md:py-20 px-6 relative overflow-hidden bg-gradient-to-b from-[#FAF7F2] via-[#F4EFEA] to-[#FAF7F2]">
    <div class="max-w-6xl mx-auto grid md:grid-cols-12 gap-12 items-center">
      <div class="md:col-span-7 space-y-6">
        <div class="inline-flex items-center gap-2 bg-white/90 border border-stone-200/90 px-4 py-1.5 rounded-full text-xs font-semibold text-[#4A6054] shadow-sm">
          <span class="w-2 h-2 rounded-full bg-[#C87D55]"></span>
          <span>6-Week Immersive Cohort • April 6 – May 17, 2026</span>
        </div>

        <h1 class="font-serif-luxury text-4xl sm:text-5xl lg:text-6xl text-stone-900 leading-[1.12] font-normal">
          Awaken from winter.<br>
          <em class="serif-italic text-[#C87D55]">Step into full bloom.</em>
        </h1>

        <p class="text-stone-600 text-lg leading-relaxed max-w-xl">
          After months of winter stillness, give your body and spirit permission to unfurl. Join our intimate sanctuary cohort for 6 weeks of somatic vinyasa flow, restorative yin, crystal sound baths, and botanical morning rituals at Bloom Room Sanctuary.
        </p>

        <div class="flex flex-wrap items-center gap-4 pt-2">
          <button type="button" onclick="artOpenModal()" class="bg-[#C87D55] hover:bg-[#B16943] text-white px-8 py-4 rounded-full font-semibold text-base shadow-lg transition flex items-center gap-2 transform hover:-translate-y-0.5">
            <span>Reserve Your Mat — Early Bird $339</span>
            <span>→</span>
          </button>
          <a href="#art-mats" class="bg-white border border-stone-300 text-[#4A6054] px-6 py-4 rounded-full font-semibold text-base hover:bg-stone-50 transition">
            View 24-Mat Floor Plan
          </a>
        </div>

        <div class="flex items-center gap-3 pt-3 text-xs text-stone-500">
          <span class="text-amber-500 text-sm">★★★★★</span>
          <span><strong>4.98 / 5</strong> from 340+ past renewal graduates</span>
          <span>•</span>
          <span>Capped at 24 mats</span>
        </div>
      </div>

      <div class="md:col-span-5 relative">
        <div class="rounded-3xl overflow-hidden shadow-2xl border border-stone-200/70 relative group">
          <img src="{HERO_B64}" alt="Bloom Room sunlit yoga sanctuary" class="w-full h-[470px] object-cover group-hover:scale-105 transition duration-700">
          <div class="absolute top-4 left-4 bg-white/95 backdrop-blur-md px-4 py-2 rounded-2xl shadow-md border border-white/70 text-xs">
            <p class="font-bold text-stone-900">🌿 Bloom Room Sanctuary</p>
            <p class="text-stone-500 text-[11px]">Natural oak, living botanicals & heated cork floors</p>
          </div>
          <div class="absolute bottom-4 right-4 bg-white/95 backdrop-blur-md px-4 py-2 rounded-2xl shadow-md border border-white/70 text-xs">
            <p class="font-bold text-stone-900">✨ Hybrid Immersion</p>
            <p class="text-stone-500 text-[11px]">In-Studio • 4K Livestream • 60-Day Replays</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Interactive 24-Mat Studio Floor Plan -->
  <section class="py-16 px-6 bg-white border-y border-stone-200" id="art-mats">
    <div class="max-w-4xl mx-auto">
      <div class="text-center mb-10">
        <span class="text-xs font-semibold uppercase tracking-widest text-[#4A6054]">Live Studio Availability</span>
        <h2 class="font-serif-luxury text-3xl sm:text-4xl text-stone-900 mt-1 font-normal">Choose Your Exact Mat Space</h2>
        <p class="text-stone-500 text-sm mt-2 max-w-xl mx-auto">
          To ensure deep personal attention and alignment adjustments, every Bloom Room cohort is strictly limited to 24 mats. Click an available mat to reserve your preferred space.
        </p>
      </div>

      <div class="bg-[#FAF7F2] p-8 rounded-3xl border border-stone-200 shadow-sm">
        <div class="flex items-center justify-between mb-6 pb-4 border-b border-stone-200 text-xs">
          <div class="flex items-center gap-6">
            <div class="flex items-center gap-2">
              <span class="w-3.5 h-3.5 rounded bg-stone-300"></span>
              <span class="text-stone-500">Reserved (18)</span>
            </div>
            <div class="flex items-center gap-2">
              <span class="w-3.5 h-3.5 rounded bg-[#C87D55] animate-pulse"></span>
              <span class="font-bold text-stone-900">Available (6)</span>
            </div>
            <div class="flex items-center gap-2">
              <span class="w-3.5 h-3.5 rounded bg-[#4A6054]"></span>
              <span class="font-bold text-[#4A6054]">Your Selection</span>
            </div>
          </div>
          <span class="text-stone-400 font-mono text-[11px]">Sanctuary Main Hall</span>
        </div>

        <!-- Instructor Stage indicator -->
        <div class="w-48 mx-auto bg-stone-200/80 text-stone-600 text-[10px] font-bold uppercase tracking-widest py-1 text-center rounded-t-lg mb-4">
          ✦ Guide Altar & Crystal Bowls ✦
        </div>

        <!-- 4 Rows x 6 Cols Mat Grid -->
        <div class="grid grid-cols-6 gap-3 sm:gap-4 max-w-2xl mx-auto" id="matGrid">
          <!-- Dynamically populated via JS -->
        </div>

        <div class="mt-6 pt-4 border-t border-stone-200 flex flex-wrap items-center justify-between gap-4">
          <div class="text-xs text-stone-600">
            <span id="matSelectionPrompt">Click any golden mat above to select your sanctuary place.</span>
          </div>
          <button type="button" id="btnMatContinue" onclick="artOpenModalWithMat()" class="bg-[#4A6054] hover:bg-[#37473E] text-white px-6 py-2.5 rounded-full text-xs font-semibold shadow-sm transition disabled:opacity-50" disabled>
            Lock In Mat & Continue →
          </button>
        </div>
      </div>
    </div>
  </section>

  <!-- Interactive Sound Healing Ambient Player -->
  <section class="py-16 px-6 bg-[#FAF7F2]" id="art-sound">
    <div class="max-w-4xl mx-auto bg-gradient-to-r from-[#37473E] to-[#4A6054] text-white rounded-3xl p-8 md:p-12 shadow-xl border border-[#2F3D35] relative overflow-hidden">
      <div class="grid md:grid-cols-12 gap-8 items-center">
        <div class="md:col-span-8 space-y-4">
          <span class="text-[10px] uppercase font-bold tracking-widest text-[#DCE3D6] bg-white/10 px-3 py-1 rounded-full">Sensory Sound Medicine</span>
          <h2 class="font-serif-luxury text-3xl sm:text-4xl text-white font-normal">Experience the 432Hz Resonance</h2>
          <p class="text-stone-200 text-sm leading-relaxed">
            Every Saturday session concludes with an alchemy sound immersion using frosted white quartz bowls. Listen to an authentic harmonic sample synthesized via the Web Audio API right in your browser.
          </p>

          <div class="flex items-center gap-4 pt-2">
            <button type="button" id="btnToggleSound" onclick="toggleSingingBowl()" class="bg-[#C87D55] hover:bg-[#B16943] text-white px-6 py-3 rounded-full text-xs font-bold tracking-wide shadow-md transition flex items-center gap-2">
              <span id="soundPlayIcon">▶</span>
              <span id="soundBtnText">Play 432Hz Crystal Sound</span>
            </button>
            <div class="flex items-end gap-1 h-6 px-3" id="soundBars">
              <span class="w-1 bg-[#DCE3D6] rounded-full bar-1 h-1.5"></span>
              <span class="w-1 bg-[#DCE3D6] rounded-full bar-2 h-2.5"></span>
              <span class="w-1 bg-[#DCE3D6] rounded-full bar-3 h-1.5"></span>
              <span class="w-1 bg-[#DCE3D6] rounded-full bar-4 h-2"></span>
              <span class="w-1 bg-[#DCE3D6] rounded-full bar-5 h-1"></span>
            </div>
            <span class="text-xs text-stone-300" id="soundStatusText">Harmonic overtone: Inactive</span>
          </div>
        </div>

        <div class="md:col-span-4">
          <div class="rounded-2xl overflow-hidden shadow-lg border border-white/20">
            <img src="{BOWL_B64}" alt="Frosted white quartz singing bowl with cherry blossoms" class="w-full h-48 object-cover">
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Complete Visual Sanctuary Gallery -->
  <section class="py-20 px-6 bg-white border-b border-stone-200" id="art-gallery">
    <div class="max-w-6xl mx-auto">
      <div class="text-center max-w-2xl mx-auto mb-16">
        <span class="text-xs font-semibold uppercase tracking-widest text-[#4A6054]">Visual Sanctuary Tour</span>
        <h2 class="font-serif-luxury text-3xl sm:text-4xl text-stone-900 mt-1 font-normal">A Glimpse Inside Bloom Room</h2>
        <p class="text-stone-500 mt-2 text-base">Architected with tactile wabi-sabi materials, gentle morning light, and living botanicals to restore your senses.</p>
      </div>

      <div class="grid md:grid-cols-12 gap-6">
        <!-- Photo 1: Large Hero Studio -->
        <div class="md:col-span-8 rounded-3xl overflow-hidden shadow-md border border-stone-200 relative group min-h-[340px]">
          <img src="{HERO_B64}" alt="Sunlit sanctuary room with plants and oak beams" class="w-full h-full object-cover group-hover:scale-105 transition duration-700">
          <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-transparent to-transparent p-6 flex flex-col justify-end text-white">
            <span class="text-[10px] uppercase font-bold tracking-widest bg-white/20 backdrop-blur-md px-2.5 py-1 rounded-full w-max mb-1">Sanctuary Main</span>
            <h3 class="font-serif-luxury text-2xl font-medium">Radiant Heated Oak Flooring & Purified Air</h3>
            <p class="text-xs text-stone-200">Non-drying infrared warmth keeps joints fluid without suffocating heat.</p>
          </div>
        </div>

        <!-- Photo 2: Instructor Crescent Pose -->
        <div class="md:col-span-4 rounded-3xl overflow-hidden shadow-md border border-stone-200 relative group min-h-[340px]">
          <img src="{INSTRUCTOR_B64}" alt="Instructor Elena demonstrating crescent stretch" class="w-full h-full object-cover group-hover:scale-105 transition duration-700">
          <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-transparent to-transparent p-6 flex flex-col justify-end text-white">
            <span class="text-[10px] uppercase font-bold tracking-widest bg-white/20 backdrop-blur-md px-2.5 py-1 rounded-full w-max mb-1">Somatic Alignment</span>
            <h3 class="font-serif-luxury text-xl font-medium">Anatomical Cueing & Grace</h3>
            <p class="text-xs text-stone-200">Respectful assists honoring your unique anatomy.</p>
          </div>
        </div>

        <!-- Photo 3: Tea Ceremony Lounge -->
        <div class="md:col-span-4 rounded-3xl overflow-hidden shadow-md border border-stone-200 relative group min-h-[320px]">
          <img src="{TEA_B64}" alt="Ceremonial teapot pouring herbal tea into clay cups" class="w-full h-full object-cover group-hover:scale-105 transition duration-700">
          <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-transparent to-transparent p-6 flex flex-col justify-end text-white">
            <span class="text-[10px] uppercase font-bold tracking-widest bg-white/20 backdrop-blur-md px-2.5 py-1 rounded-full w-max mb-1">Tea Lounge</span>
            <h3 class="font-serif-luxury text-xl font-medium">Botanical Spring Infusions</h3>
            <p class="text-xs text-stone-200">Steamed jasmine, nettle & chamomile post-class.</p>
          </div>
        </div>

        <!-- Photo 4: Singing Bowl by Cherry Blossom Window -->
        <div class="md:col-span-4 rounded-3xl overflow-hidden shadow-md border border-stone-200 relative group min-h-[320px]">
          <img src="{BOWL_B64}" alt="Frosted crystal singing bowl with spring flowers" class="w-full h-full object-cover group-hover:scale-105 transition duration-700">
          <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-transparent to-transparent p-6 flex flex-col justify-end text-white">
            <span class="text-[10px] uppercase font-bold tracking-widest bg-white/20 backdrop-blur-md px-2.5 py-1 rounded-full w-max mb-1">Sound Alchemy</span>
            <h3 class="font-serif-luxury text-xl font-medium">432Hz Quartz Singing Bowls</h3>
            <p class="text-xs text-stone-200">Deep parasympathetic nervous system release.</p>
          </div>
        </div>

        <!-- Photo 5: Journal & Singing Bowl on Limestone -->
        <div class="md:col-span-4 rounded-3xl overflow-hidden shadow-md border border-stone-200 relative group min-h-[320px]">
          <img src="{RITUAL_B64}" alt="Gratitude journal with brass pen, tea and crystal bowl" class="w-full h-full object-cover group-hover:scale-105 transition duration-700">
          <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-transparent to-transparent p-6 flex flex-col justify-end text-white">
            <span class="text-[10px] uppercase font-bold tracking-widest bg-white/20 backdrop-blur-md px-2.5 py-1 rounded-full w-max mb-1">Mindful Inquiry</span>
            <h3 class="font-serif-luxury text-xl font-medium">Reflective Journal Prompts</h3>
            <p class="text-xs text-stone-200">Weekly contemplation questions to deepen growth.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Interactive 6-Week Curriculum Section -->
  <section class="py-20 px-6" id="art-curriculum">
    <div class="max-w-6xl mx-auto">
      <div class="text-center max-w-2xl mx-auto mb-12">
        <span class="text-xs font-semibold uppercase tracking-widest text-[#4A6054]">Weekly Transformation Arc</span>
        <h2 class="font-serif-luxury text-3xl sm:text-4xl text-stone-900 mt-2 font-normal">The 6-Week Progressive Journey</h2>
        <p class="text-stone-500 mt-3 text-base">Select any week below to explore the thematic movement, breathwork, soundscape, and take-home rituals.</p>
      </div>

      <!-- Tab Buttons -->
      <div class="flex flex-wrap justify-center gap-2 mb-8 bg-stone-200/60 p-1.5 rounded-full max-w-3xl mx-auto">
        <button onclick="artSelectWeek(1)" id="tab-1" class="week-tab-btn active px-4 py-2 rounded-full text-xs font-bold transition bg-[#4A6054] text-white shadow-sm">Week 1: Ground</button>
        <button onclick="artSelectWeek(2)" id="tab-2" class="week-tab-btn px-4 py-2 rounded-full text-xs font-bold transition text-stone-600 hover:text-stone-900">Week 2: Fluid Detox</button>
        <button onclick="artSelectWeek(3)" id="tab-3" class="week-tab-btn px-4 py-2 rounded-full text-xs font-bold transition text-stone-600 hover:text-stone-900">Week 3: Ignite</button>
        <button onclick="artSelectWeek(4)" id="tab-4" class="week-tab-btn px-4 py-2 rounded-full text-xs font-bold transition text-stone-600 hover:text-stone-900">Week 4: Heart Open</button>
        <button onclick="artSelectWeek(5)" id="tab-5" class="week-tab-btn px-4 py-2 rounded-full text-xs font-bold transition text-stone-600 hover:text-stone-900">Week 5: Sound Bath</button>
        <button onclick="artSelectWeek(6)" id="tab-6" class="week-tab-btn px-4 py-2 rounded-full text-xs font-bold transition text-stone-600 hover:text-stone-900">Week 6: Full Bloom</button>
      </div>

      <!-- Dynamic Curriculum Card -->
      <div class="bg-white rounded-3xl p-8 md:p-12 border border-stone-200 shadow-xl grid md:grid-cols-12 gap-8 items-center" id="artCurriculumBox">
        <div class="md:col-span-7 space-y-4">
          <span class="text-xs font-bold uppercase tracking-wider text-[#C87D55]" id="artWeekBadge">Week 1 • Prithvi (Earth Archetype)</span>
          <h3 class="font-serif-luxury text-3xl font-medium text-stone-900" id="artWeekTitle">Awaken & Ground</h3>
          <p class="text-stone-600 text-sm leading-relaxed" id="artWeekDesc">Emerge from winter hibernation by anchoring stability into the feet, pelvic bowl, and lower spine. We begin with mindful fascial hydration and gentle joint unwinding before upward expansion.</p>

          <div class="grid sm:grid-cols-2 gap-3 pt-2">
            <div class="bg-[#FAF7F2] p-3.5 rounded-xl border border-stone-200/80">
              <strong class="text-xs text-[#4A6054] uppercase tracking-wider block mb-1">Movement Practice</strong>
              <p class="text-xs text-stone-600" id="artWeekMove">Low-center grounding vinyasa, standing root holds, and gentle hip capsule mobility.</p>
            </div>
            <div class="bg-[#FAF7F2] p-3.5 rounded-xl border border-stone-200/80">
              <strong class="text-xs text-[#4A6054] uppercase tracking-wider block mb-1">Breathwork</strong>
              <p class="text-xs text-stone-600" id="artWeekBreath">Dirga Pranayama (Three-Part Breath) with tactile lower belly awareness.</p>
            </div>
            <div class="bg-[#FAF7F2] p-3.5 rounded-xl border border-stone-200/80">
              <strong class="text-xs text-[#4A6054] uppercase tracking-wider block mb-1">Sound & Sensory</strong>
              <p class="text-xs text-stone-600" id="artWeekSound">Warm grounding Tibetan brass bowls and cedarwood essential mist.</p>
            </div>
            <div class="bg-[#FAF7F2] p-3.5 rounded-xl border border-stone-200/80">
              <strong class="text-xs text-[#4A6054] uppercase tracking-wider block mb-1">Weekly Gift</strong>
              <p class="text-xs text-stone-600" id="artWeekGift">Bloom Room Natural Cork Fascial Sphere for home unwinding.</p>
            </div>
          </div>

          <div class="bg-[#F9EBE3] border-l-4 border-[#C87D55] p-3.5 rounded-r-xl text-xs italic text-[#B16943]">
            <strong>Reflective Prompt:</strong> <span id="artWeekPrompt">"Where in my body and life am I still carrying winter heaviness, and what foundation am I ready to build upon?"</span>
          </div>
        </div>

        <div class="md:col-span-5 bg-[#FAF7F2] p-6 rounded-2xl border border-stone-200 space-y-4">
          <h4 class="font-serif-luxury text-xl font-medium text-stone-900">Key Focus Sessions This Week</h4>
          <ul class="text-xs text-stone-600 space-y-2.5" id="artWeekList">
            <li class="flex items-center gap-2"><span class="text-[#C87D55]">✦</span> Foot & Ankle Fascial Awakening</li>
            <li class="flex items-center gap-2"><span class="text-[#C87D55]">✦</span> Slow Grounding Vinyasa (Root Chakra)</li>
            <li class="flex items-center gap-2"><span class="text-[#C87D55]">✦</span> Nervous System Orienting Exercise</li>
            <li class="flex items-center gap-2"><span class="text-[#C87D55]">✦</span> Introduction to the Seasonal Journal</li>
          </ul>
          <button type="button" onclick="artOpenModal()" class="w-full bg-[#4A6054] hover:bg-[#37473E] text-white py-3 rounded-full text-xs font-semibold shadow-md transition">
            Reserve for This Cohort
          </button>
        </div>
      </div>
    </div>
  </section>

  <!-- Interactive Renewal Quiz -->
  <section class="py-20 px-6 bg-[#4A6054] text-white" id="art-quiz">
    <div class="max-w-3xl mx-auto">
      <div class="text-center mb-10">
        <span class="text-xs font-semibold uppercase tracking-widest text-[#DCE3D6]">Self-Assessment</span>
        <h2 class="font-serif-luxury text-3xl sm:text-4xl text-white mt-1 font-normal">Discover Your Spring Renewal Path</h2>
        <p class="text-stone-200 text-sm mt-2">Answer 3 brief questions to reveal your personalized class track and botanical pairing.</p>
      </div>

      <div class="bg-white text-stone-800 rounded-3xl p-8 md:p-10 shadow-2xl">
        <!-- Question 1 -->
        <div id="quiz-q1" class="space-y-4">
          <span class="text-xs font-bold uppercase tracking-wider text-[#C87D55]">Question 1 of 3</span>
          <h3 class="font-serif-luxury text-2xl font-medium">How does your body and mental space feel right now?</h3>
          <div class="grid gap-3 pt-2">
            <button onclick="artQuizAnswer('stiff')" class="text-left p-4 rounded-xl border border-stone-200 hover:border-[#4A6054] hover:bg-stone-50 transition">
              <strong class="block text-sm text-stone-900">Sluggish & Stiff</strong>
              <span class="text-xs text-stone-500">Winter stiffness, tight lower back or hips, craving physical mobility.</span>
            </button>
            <button onclick="artQuizAnswer('stressed')" class="text-left p-4 rounded-xl border border-stone-200 hover:border-[#4A6054] hover:bg-stone-50 transition">
              <strong class="block text-sm text-stone-900">Wired & Mentally Overwhelmed</strong>
              <span class="text-xs text-stone-500">High cognitive fatigue, shallow breathing, craving deep restorative silence.</span>
            </button>
            <button onclick="artQuizAnswer('stagnant')" class="text-left p-4 rounded-xl border border-stone-200 hover:border-[#4A6054] hover:bg-stone-50 transition">
              <strong class="block text-sm text-stone-900">Seeking Vitality & Dynamic Stamina</strong>
              <span class="text-xs text-stone-500">Ready to build vibrant physical strength, core grace, and creative energy.</span>
            </button>
          </div>
        </div>

        <!-- Result View (hidden by default) -->
        <div id="quiz-result-view" style="display: none;" class="space-y-5">
          <div class="inline-block bg-[#F9EBE3] text-[#B16943] text-xs font-bold px-3 py-1 rounded-full">✨ Your Tailored Plan</div>
          <h3 class="font-serif-luxury text-3xl font-medium text-stone-900" id="artQuizResTitle">The Somatic Reset & Mobility Track</h3>
          <p class="text-stone-600 text-sm leading-relaxed" id="artQuizResDesc">Based on your answers, your body is primed to release winter stagnation with spiral mobility flows and nervous system toning.</p>
          
          <div class="bg-[#FAF7F2] p-4 rounded-2xl border border-stone-200 space-y-2 text-xs">
            <p><strong>🧘 Suggested Cadence:</strong> <span id="artQuizCadence">2 Morning Solar Flows + 1 Twilight Yin & Sound Bath weekly</span></p>
            <p><strong>🌿 Botanical Synergy:</strong> <span id="artQuizHerb">Organic meadowsweet, turmeric, and fresh ginger spring tonic</span></p>
            <p><strong>🏷️ Recommended Tier:</strong> <span id="artQuizTier">The Full Bloom ($439) — Includes Welcome Box & 1:1 Consult</span></p>
          </div>

          <div class="flex gap-3 pt-2">
            <button onclick="artOpenModal()" class="bg-[#C87D55] hover:bg-[#B16943] text-white px-6 py-2.5 rounded-full text-xs font-semibold shadow-md transition">
              Apply This Plan to Enrollment
            </button>
            <button onclick="artResetQuiz()" class="text-stone-500 hover:text-stone-800 text-xs font-medium px-4 py-2">
              Retake Quiz
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Tuition & Pricing Section -->
  <section class="py-20 px-6 bg-[#FAF7F2]" id="art-investment">
    <div class="max-w-6xl mx-auto">
      <div class="text-center max-w-2xl mx-auto mb-16">
        <span class="text-xs font-semibold uppercase tracking-widest text-[#4A6054]">Program Tuition</span>
        <h2 class="font-serif-luxury text-3xl sm:text-4xl text-stone-900 mt-2 font-normal">Choose Your Immersion Level</h2>
        <p class="text-stone-500 mt-3 text-base">Early-bird pricing is active until April 2. All tiers include full access to the member portal and our 14-day schedule guarantee.</p>
      </div>

      <div class="grid md:grid-cols-3 gap-8">
        <!-- Tier 1 -->
        <div class="bg-white rounded-3xl p-8 border border-stone-200 shadow-sm flex flex-col justify-between hover:shadow-md transition">
          <div>
            <span class="text-[10px] font-bold uppercase tracking-wider bg-stone-100 text-stone-600 px-3 py-1 rounded-full">In-Studio Core</span>
            <h3 class="font-serif-luxury text-2xl font-medium text-stone-900 mt-3">Sanctuary Rhythm</h3>
            <p class="text-xs text-stone-500 mt-1 mb-4">Ideal for students wanting 2 foundational in-studio practices a week.</p>
            <div class="text-4xl font-bold text-stone-900 font-sans mb-1">$339</div>
            <span class="text-xs text-[#4A6054] font-semibold">Early Bird (Save $50)</span>

            <ul class="text-xs text-stone-600 space-y-3 mt-6 border-t border-stone-100 pt-6">
              <li>✓ 12 In-Studio sessions (2x weekly)</li>
              <li>✓ Full On-Demand Library with 60-day access</li>
              <li>✓ Digital Spring Renewal Workbook & Prompts</li>
              <li>✓ Post-practice botanical tea lounge</li>
            </ul>
          </div>
          <button onclick="artOpenModal('Sanctuary Rhythm')" class="w-full mt-8 border border-[#4A6054] text-[#4A6054] hover:bg-[#4A6054] hover:text-white py-3 rounded-full text-xs font-semibold transition">
            Select Sanctuary Rhythm
          </button>
        </div>

        <!-- Tier 2 (Featured) -->
        <div class="bg-white rounded-3xl p-8 border-2 border-[#C87D55] shadow-xl flex flex-col justify-between relative transform md:-translate-y-2">
          <div class="absolute -top-3.5 left-1/2 -translate-x-1/2 bg-[#C87D55] text-white text-[10px] font-bold uppercase tracking-widest px-4 py-1 rounded-full shadow-sm">
            Most Transformative
          </div>
          <div>
            <span class="text-[10px] font-bold uppercase tracking-wider bg-[#F9EBE3] text-[#B16943] px-3 py-1 rounded-full">Complete Immersion</span>
            <h3 class="font-serif-luxury text-2xl font-medium text-stone-900 mt-3">The Full Bloom</h3>
            <p class="text-xs text-stone-500 mt-1 mb-4">Our flagship cohort experience for complete somatic reset and vitality.</p>
            <div class="text-4xl font-bold text-stone-900 font-sans mb-1">$439</div>
            <span class="text-xs text-[#C87D55] font-semibold">Early Bird (Save $50)</span>

            <ul class="text-xs text-stone-700 space-y-3 mt-6 border-t border-stone-100 pt-6">
              <li>✓ <strong>18 In-Studio sessions</strong> (3x weekly flexibility)</li>
              <li>✓ <strong>Bloom Room Physical Welcome Box</strong> ($120 value: cork roller, linen eye pillow, tea)</li>
              <li>✓ <strong>2 Saturday Twilight Sound Baths</strong> included</li>
              <li>✓ <strong>1:1 30-min Alignment Consult</strong> with Elena Rostova</li>
              <li>✓ Priority front-row mat reservation</li>
            </ul>
          </div>
          <button onclick="artOpenModal('The Full Bloom')" class="w-full mt-8 bg-[#C87D55] hover:bg-[#B16943] text-white py-3 rounded-full text-xs font-semibold shadow-md transition">
            Select The Full Bloom
          </button>
        </div>

        <!-- Tier 3 -->
        <div class="bg-white rounded-3xl p-8 border border-stone-200 shadow-sm flex flex-col justify-between hover:shadow-md transition">
          <div>
            <span class="text-[10px] font-bold uppercase tracking-wider bg-stone-100 text-stone-600 px-3 py-1 rounded-full">Remote / Anywhere</span>
            <h3 class="font-serif-luxury text-2xl font-medium text-stone-900 mt-3">Digital Sanctuary</h3>
            <p class="text-xs text-stone-500 mt-1 mb-4">For remote yogis or frequent travelers seeking structured seasonal renewal from home.</p>
            <div class="text-4xl font-bold text-stone-900 font-sans mb-1">$189</div>
            <span class="text-xs text-[#4A6054] font-semibold">Early Bird (Save $40)</span>

            <ul class="text-xs text-stone-600 space-y-3 mt-6 border-t border-stone-100 pt-6">
              <li>✓ 18 Multi-camera 4K HD Livestreams</li>
              <li>✓ On-demand replays available within 2 hours</li>
              <li>✓ Binaural audio sound healing tracks</li>
              <li>✓ Printable Renewal Journal & Home Ritual Guide</li>
            </ul>
          </div>
          <button onclick="artOpenModal('Digital Sanctuary')" class="w-full mt-8 border border-[#4A6054] text-[#4A6054] hover:bg-[#4A6054] hover:text-white py-3 rounded-full text-xs font-semibold transition">
            Select Digital Sanctuary
          </button>
        </div>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="bg-[#242B26] text-stone-300 py-12 px-6 text-xs">
    <div class="max-w-6xl mx-auto flex flex-col md:flex-row justify-between items-center gap-6 border-b border-white/10 pb-8 mb-8">
      <div>
        <span class="font-serif-luxury text-xl font-bold tracking-widest text-white block">BLOOM ROOM</span>
        <span class="text-[10px] tracking-widest text-stone-400 block mt-0.5">YOGA & SANCTUARY • MILL VALLEY, CA</span>
      </div>
      <div class="flex gap-6 text-stone-400">
        <a href="#art-curriculum" class="hover:text-white transition">Curriculum</a>
        <a href="#art-gallery" class="hover:text-white transition">Gallery</a>
        <a href="#art-mats" class="hover:text-white transition">Studio Floor Plan</a>
        <a href="#art-investment" class="hover:text-white transition">Tuition</a>
      </div>
    </div>
    <div class="max-w-6xl mx-auto flex flex-col sm:flex-row justify-between items-center text-stone-500 gap-4">
      <p>© 2026 Bloom Room Yoga Sanctuary LLC. All rights reserved.</p>
      <p>428 Blossom Way • Mill Valley, CA • hello@bloomroomyoga.com</p>
    </div>
  </footer>

  <!-- Modal -->
  <div id="artModal" class="fixed inset-0 bg-black/60 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4">
    <div class="bg-white rounded-3xl max-w-md w-full p-6 shadow-2xl relative">
      <button onclick="artCloseModal()" class="absolute top-4 right-4 w-8 h-8 rounded-full bg-stone-100 text-stone-600 flex items-center justify-center text-sm font-bold hover:bg-stone-200">✕</button>

      <div id="artModalStep1">
        <span class="text-[10px] font-bold uppercase tracking-wider text-[#C87D55]">Spring Renewal 2026</span>
        <h3 class="font-serif-luxury text-2xl font-medium text-stone-900 mt-1 mb-2">Reserve Your Mat</h3>
        <p class="text-xs text-stone-500 mb-4">Complete your reservation for the 6-week cohort beginning April 6.</p>

        <form onsubmit="artSubmitReservation(event)" class="space-y-3">
          <div>
            <label class="block text-[11px] font-bold text-stone-700 uppercase mb-1">Selected Mat Space</label>
            <input type="text" id="artModalMatDisplay" readonly value="Mat #4 (Center Sanctuary)" class="w-full text-xs p-2.5 rounded-xl border border-stone-200 bg-stone-100 font-semibold text-[#4A6054]">
          </div>

          <div>
            <label class="block text-[11px] font-bold text-stone-700 uppercase mb-1">Select Tier</label>
            <select id="artModalTier" class="w-full text-xs p-2.5 rounded-xl border border-stone-200 bg-stone-50">
              <option value="The Full Bloom ($439)" selected>The Full Bloom ($439) — Most Popular</option>
              <option value="Sanctuary Rhythm ($339)">Sanctuary Rhythm ($339)</option>
              <option value="Digital Sanctuary ($189)">Digital Sanctuary ($189)</option>
            </select>
          </div>

          <div>
            <label class="block text-[11px] font-bold text-stone-700 uppercase mb-1">Your Name</label>
            <input type="text" id="artCustName" required placeholder="Elena Vance" class="w-full text-xs p-2.5 rounded-xl border border-stone-200 bg-stone-50">
          </div>

          <div>
            <label class="block text-[11px] font-bold text-stone-700 uppercase mb-1">Email Address</label>
            <input type="email" id="artCustEmail" required placeholder="elena@example.com" class="w-full text-xs p-2.5 rounded-xl border border-stone-200 bg-stone-50">
          </div>

          <button type="submit" class="w-full bg-[#C87D55] hover:bg-[#B16943] text-white py-3 rounded-full text-xs font-semibold shadow-md transition mt-2">
            Confirm My Mat Reservation
          </button>
        </form>
      </div>

      <div id="artModalStep2" style="display: none;" class="text-center py-4 space-y-3">
        <div class="text-4xl">🌸</div>
        <h3 class="font-serif-luxury text-2xl font-medium text-stone-900">Your Mat is Reserved!</h3>
        <p class="text-xs text-stone-600">Welcome to Bloom Room! We've sent your welcome onboarding packet and orientation details to <strong id="artConfEmail">your email</strong>.</p>
        <button onclick="artCloseModal()" class="bg-[#4A6054] text-white px-6 py-2 rounded-full text-xs font-semibold mt-2">
          Done
        </button>
      </div>
    </div>
  </div>

  <script>
    // Live countdown simulation
    const artTimerEl = document.getElementById('artTimer');
    if (artTimerEl) {{
      let seconds = 30, minutes = 48, hours = 12, days = 4;
      setInterval(() => {{
        if (--seconds < 0) {{ seconds = 59; minutes--; }}
        if (minutes < 0) {{ minutes = 59; hours--; }}
        artTimerEl.textContent = `0${{days}}d : ${{hours}}h : ${{minutes}}m : ${{seconds < 10 ? '0' + seconds : seconds}}s`;
      }}, 1000);
    }}

    // Mat Floor Plan Logic
    let selectedMatNum = 4;
    const availableMats = [4, 7, 11, 16, 21, 24];

    function renderMatGrid() {{
      const grid = document.getElementById('matGrid');
      if (!grid) return;
      grid.innerHTML = '';

      for (let i = 1; i <= 24; i++) {{
        const isAvail = availableMats.includes(i);
        const isSelected = selectedMatNum === i;
        const btn = document.createElement('button');
        btn.type = 'button';
        btn.className = `p-2.5 rounded-xl text-center text-xs font-bold transition flex flex-col items-center justify-center border ${{
          isSelected ? 'bg-[#4A6054] text-white border-[#4A6054] shadow-md scale-105' :
          isAvail ? 'bg-[#C87D55] text-white border-[#C87D55] hover:scale-105 shadow-xs cursor-pointer animate-pulse' :
          'bg-stone-200 text-stone-400 border-stone-200 cursor-not-allowed opacity-60'
        }}`;
        btn.innerHTML = `<span class="text-[9px] uppercase tracking-wider block mb-0.5">Mat</span><span class="text-sm">${{i}}</span>`;
        if (isAvail) {{
          btn.onclick = () => selectMat(i);
        }}
        grid.appendChild(btn);
      }}
    }}

    function selectMat(num) {{
      selectedMatNum = num;
      renderMatGrid();
      const prompt = document.getElementById('matSelectionPrompt');
      const btnContinue = document.getElementById('btnMatContinue');
      const display = document.getElementById('artModalMatDisplay');
      if (prompt) prompt.innerHTML = `✨ <strong>Mat #${{num}}</strong> selected! (Row ${{Math.ceil(num/6)}}, Space ${{((num-1)%6)+1}})`;
      if (btnContinue) btnContinue.disabled = false;
      if (display) display.value = `Mat #${{num}} (Row ${{Math.ceil(num/6)}}, Space ${{((num-1)%6)+1}})`;
    }}

    function artOpenModalWithMat() {{
      artOpenModal();
    }}

    renderMatGrid();

    // 432Hz Web Audio Singing Bowl Generator
    let audioCtx = null;
    let isPlayingSound = false;
    let osc1 = null, osc2 = null, gainNode = null;

    function toggleSingingBowl() {{
      if (isPlayingSound) {{
        stopSingingBowl();
      }} else {{
        startSingingBowl();
      }}
    }}

    function startSingingBowl() {{
      try {{
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        gainNode = audioCtx.createGain();
        gainNode.gain.setValueAtTime(0.01, audioCtx.currentTime);
        gainNode.gain.exponentialRampToValueAtTime(0.18, audioCtx.currentTime + 1.5);
        gainNode.connect(audioCtx.destination);

        // 432Hz fundamental
        osc1 = audioCtx.createOscillator();
        osc1.type = 'sine';
        osc1.frequency.setValueAtTime(432, audioCtx.currentTime);
        osc1.connect(gainNode);

        // Harmonic overtone 864Hz with subtle detune
        osc2 = audioCtx.createOscillator();
        osc2.type = 'sine';
        osc2.frequency.setValueAtTime(864.8, audioCtx.currentTime);
        osc2.connect(gainNode);

        osc1.start();
        osc2.start();

        isPlayingSound = true;
        document.getElementById('soundBtnText').textContent = 'Pause 432Hz Tone';
        document.getElementById('soundPlayIcon').textContent = '⏸';
        document.getElementById('soundStatusText').textContent = 'Harmonic overtone: Active (432Hz Resonance)';
        document.getElementById('soundBars').classList.add('sound-active');
      }} catch(e) {{
        console.error(e);
      }}
    }}

    function stopSingingBowl() {{
      if (gainNode && audioCtx) {{
        gainNode.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.8);
        setTimeout(() => {{
          if (osc1) osc1.stop();
          if (osc2) osc2.stop();
          if (audioCtx) audioCtx.close();
          isPlayingSound = false;
          document.getElementById('soundBtnText').textContent = 'Play 432Hz Crystal Sound';
          document.getElementById('soundPlayIcon').textContent = '▶';
          document.getElementById('soundStatusText').textContent = 'Harmonic overtone: Paused';
          document.getElementById('soundBars').classList.remove('sound-active');
        }}, 800);
      }}
    }}

    // Curriculum data
    const artWeeks = {{
      1: {{
        badge: "Week 1 • Prithvi (Earth Archetype)",
        title: "Awaken & Ground",
        desc: "Emerge from winter hibernation by anchoring stability into the feet, pelvic bowl, and lower spine. We begin with mindful fascial hydration and gentle joint unwinding before upward expansion.",
        move: "Low-center grounding vinyasa, standing root holds, and gentle hip capsule mobility.",
        breath: "Dirga Pranayama (Three-Part Breath) with tactile lower belly awareness.",
        sound: "Warm grounding Tibetan brass bowls and cedarwood essential mist.",
        gift: "Bloom Room Natural Cork Fascial Sphere for home unwinding.",
        prompt: "\\"Where in my body and life am I still carrying winter heaviness, and what foundation am I ready to build upon?\\"",
        list: ["Foot & Ankle Fascial Awakening", "Slow Grounding Vinyasa (Root Chakra)", "Nervous System Orienting Exercise", "Introduction to the Seasonal Journal"]
      }},
      2: {{
        badge: "Week 2 • Jala (Water Archetype)",
        title: "Fluid Mobility & Detox",
        desc: "Encourage natural lymphatic circulation and spinal decompression through spiraling, organic flows to lubricate synovial joints and melt stagnant connective tissue.",
        move: "Spiral pelvic sways, rhythmic sun salutations, thoracic rotation, and restorative side-body lengthening.",
        breath: "Nadi Shodhana (Alternate Nostril Breathing) to harmonize brain hemispheres.",
        sound: "Flowing koshi wind chimes and tuned crystal bowls evoking river currents.",
        gift: "Organic botanical dandelion & lemongrass spring lymphatic tea blend.",
        prompt: "\\"Where am I gripping or resisting natural change, and how can I bring more fluid adaptability to my days?\\"",
        list: ["Lymphatic Pump Flow & Gentle Inversions", "Spinal Wave Decompression", "Hydration & Spring Herbology Circle", "Evening Candlelit Hip Opening"]
      }},
      3: {{
        badge: "Week 3 • Agni (Fire Archetype)",
        title: "Ignite Vitality & Inner Sun",
        desc: "Kindle the transformative internal fire of the solar plexus (Manipura). Build lean physical stamina, core buoyancy, and focused determination without tipping into burnout.",
        move: "Dynamic standing balance series, solar vinyasa pacing, intelligent core integration, and warrior expansions.",
        breath: "Kapalabhati (Skull-Shining Breath) followed by Kumbhaka retention practice.",
        sound: "Resonant brass gongs and solar quartz crystal tones.",
        gift: "Aromatherapy Solar Roll-On: ginger, bergamot & sweet orange.",
        prompt: "\\"What creative spark or healthy habit is ready to be fed with steady, disciplined enthusiasm?\\"",
        list: ["Core Center & Psoas Awareness", "Power & Grace Balance Transitions", "Digestive Health & Agni Lecture", "Twilight Cooling Yin Counterbalance"]
      }},
      4: {{
        badge: "Week 4 • Anahata (Heart & Air Archetype)",
        title: "Heart Opening & Spacious Breath",
        desc: "Release habitual protective hunching, tight pectorals, and shallow upper-chest breathing. Cultivate expansive shoulder mobility, supported gentle backbends, and emotional spaciousness.",
        move: "Bolster-supported fish pose, camel pose variations, prone cobra waves, and shoulder flossing.",
        breath: "Anahata heart coherence breathing with 5.5-second rhythm.",
        sound: "528Hz crystal singing bowl known for heart resonance.",
        gift: "Handmade organic linen lavender eye pillow for savasana.",
        prompt: "\\"What armor around my heart am I safe to soften now, and what compassion can I extend toward myself?\\"",
        list: ["Shoulder Girdle & Upper Spine Unwinding", "Supported Backbend Exploration", "Metta (Loving-Kindness) Meditation", "Post-Class Herbal Rose Tisane"]
      }},
      5: {{
        badge: "Week 5 • Akasha (Space & Sound Archetype)",
        title: "Sound Alchemy & Vagus Release",
        desc: "Delve into restorative yoga postures held for 6–10 minutes with full prop support, combined with a therapeutic sound bath to stimulate the vagus nerve and promote cellular regeneration.",
        move: "Supported floor yin postures, legs-up-the-wall inversion, and neck somatic de-armoring.",
        breath: "Bhramari (Humming Bee Breath) to tone the vagal pathways.",
        sound: "Complete 432Hz frosted quartz singing bowl sound bath immersion.",
        gift: "Bloom Room Ceremonial Palo Santo & Jasmine Room Mist.",
        prompt: "\\"In the spacious quiet between my thoughts, what gentle wisdom is waiting to be heard?\\"",
        list: ["90-Minute Restorative Yin Sanctuary", "Therapeutic Sound Immersion Experience", "Vagus Nerve Health Education", "Silent Walking Meditation"]
      }},
      6: {{
        badge: "Week 6 • Sahasrara (Full Bloom Archetype)",
        title: "Full Bloom & Integration",
        desc: "Celebrate six weeks of dedicated transformation. Consolidate your physical strength, renewed vitality, and mental peace into an enduring sustainable personal home practice.",
        move: "Graceful celebratory flow weaving together elements of all previous weeks, followed by deep savasana.",
        breath: "Sama Vritti (Equal Ratio Breath) and open-awareness meditation.",
        sound: "Harmonic choir of singing bowls and closing gong circle.",
        gift: "Hand-thrown ceramic Bloom Room tea cup and cohort diploma.",
        prompt: "\\"Who have I grown into over these six weeks, and how will I carry this calm radiance into the world?\\"",
        list: ["Integration Masterclass (All Faculty)", "Building Your 15-Minute Home Ritual", "Cohort Closing Ceremony & Cacao", "Alumni Community Circle Access"]
      }}
    }};

    function artSelectWeek(num) {{
      document.querySelectorAll('.week-tab-btn').forEach((b, idx) => {{
        if (idx + 1 === num) {{
          b.className = "week-tab-btn active px-4 py-2 rounded-full text-xs font-bold transition bg-[#4A6054] text-white shadow-sm";
        }} else {{
          b.className = "week-tab-btn px-4 py-2 rounded-full text-xs font-bold transition text-stone-600 hover:text-stone-900";
        }}
      }});

      const d = artWeeks[num];
      if (!d) return;
      document.getElementById('artWeekBadge').textContent = d.badge;
      document.getElementById('artWeekTitle').textContent = d.title;
      document.getElementById('artWeekDesc').textContent = d.desc;
      document.getElementById('artWeekMove').textContent = d.move;
      document.getElementById('artWeekBreath').textContent = d.breath;
      document.getElementById('artWeekSound').textContent = d.sound;
      document.getElementById('artWeekGift').textContent = d.gift;
      document.getElementById('artWeekPrompt').textContent = d.prompt;
      
      const listEl = document.getElementById('artWeekList');
      listEl.innerHTML = d.list.map(item => `<li class="flex items-center gap-2"><span class="text-[#C87D55]">✦</span> ${{item}}</li>`).join('');
    }}

    // Quiz logic
    function artQuizAnswer(type) {{
      document.getElementById('quiz-q1').style.display = 'none';
      document.getElementById('quiz-result-view').style.display = 'block';

      if (type === 'stressed') {{
        document.getElementById('artQuizResTitle').textContent = "The Nervous System Calming & Sound Track";
        document.getElementById('artQuizResDesc').textContent = "Your adrenals and mind are asking for restorative quiet, parasympathetic toning, and sound vibration to discharge accumulated winter stress.";
        document.getElementById('artQuizCadence').textContent = "2 Twilight Restorative Yin & Sound Alchemy + 1 Weekend Immersion";
        document.getElementById('artQuizHerb').textContent = "Organic passionflower, holy basil (tulsi), and chamomile blossom";
        document.getElementById('artQuizTier').textContent = "The Full Bloom ($439) — Includes 2 Saturday Candlelight Sound Baths";
      }} else if (type === 'stagnant') {{
        document.getElementById('artQuizResTitle').textContent = "The Vitality, Core & Inner Sun Track";
        document.getElementById('artQuizResDesc').textContent = "You are primed to build physical agility, core stamina, and creative fire as the days lengthen.";
        document.getElementById('artQuizCadence').textContent = "3 Morning Solar Flows + Saturday Cohort Masterclass";
        document.getElementById('artQuizHerb').textContent = "Ceremonial matcha, gotu kola, and fresh lemongrass infusion";
        document.getElementById('artQuizTier').textContent = "Sanctuary Rhythm ($339) or The Full Bloom ($439)";
      }}
    }}

    function artResetQuiz() {{
      document.getElementById('quiz-q1').style.display = 'block';
      document.getElementById('quiz-result-view').style.display = 'none';
    }}

    // Modal
    function artOpenModal(tier) {{
      const modal = document.getElementById('artModal');
      modal.classList.remove('hidden');
      document.getElementById('artModalStep1').style.display = 'block';
      document.getElementById('artModalStep2').style.display = 'none';
      if (tier) {{
        const select = document.getElementById('artModalTier');
        for (let i = 0; i < select.options.length; i++) {{
          if (select.options[i].value.includes(tier)) {{
            select.selectedIndex = i;
            break;
          }}
        }}
      }}
    }}

    function artCloseModal() {{
      document.getElementById('artModal').classList.add('hidden');
    }}

    function artSubmitReservation(e) {{
      e.preventDefault();
      const email = document.getElementById('artCustEmail').value;
      document.getElementById('artConfEmail').textContent = email;
      document.getElementById('artModalStep1').style.display = 'none';
      document.getElementById('artModalStep2').style.display = 'block';
    }}
  </script>
</body>
</html>
"""

with open(os.path.join(artifact_dir, 'bloom_room_landing_page.html'), 'w') as f:
    f.write(html_artifact)
print("Updated bloom_room_landing_page.html with all 5 base64 images, 24-mat floor plan, and 432Hz sound player.")


# ==============================================================================
# 2. BUILD COMPACT INLINE WIDGET (bloom_room_widget.html)
# ==============================================================================
html_widget = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
</head>
<body class="bg-transparent text-[var(--foreground)] antialiased p-0 m-0 font-sans">
  <div class="py-2 space-y-3">
    <!-- Header with Live Badge -->
    <div class="flex items-center justify-between pb-2 border-b border-[var(--card-border)] text-xs">
      <div class="flex items-center gap-2">
        <span class="w-2.5 h-2.5 rounded-full bg-[#C87D55] animate-pulse"></span>
        <span class="font-bold text-[var(--foreground)] uppercase tracking-wider">Bloom Room • Spring Renewal 2026</span>
      </div>
      <span class="bg-[#C87D55]/15 text-[#C87D55] font-semibold px-2 py-0.5 rounded-full">6 of 24 Mats Left</span>
    </div>

    <!-- Mode Selector Tabs -->
    <div class="grid grid-cols-4 gap-1 bg-[var(--content)]/40 p-1 rounded-xl text-xs font-semibold">
      <button onclick="setTab('gallery')" id="btn-gallery" class="py-1.5 px-2 rounded-lg bg-[var(--card)] text-[var(--foreground)] shadow-xs transition text-center">
        Sanctuary
      </button>
      <button onclick="setTab('curriculum')" id="btn-curriculum" class="py-1.5 px-2 rounded-lg text-[var(--muted-foreground)] hover:text-[var(--foreground)] transition text-center">
        6 Weeks
      </button>
      <button onclick="setTab('mats')" id="btn-mats" class="py-1.5 px-2 rounded-lg text-[var(--muted-foreground)] hover:text-[var(--foreground)] transition text-center">
        Floor Plan
      </button>
      <button onclick="setTab('sound')" id="btn-sound" class="py-1.5 px-2 rounded-lg text-[var(--muted-foreground)] hover:text-[var(--foreground)] transition text-center">
        432Hz Sound
      </button>
    </div>

    <!-- Tab 1: Visual Sanctuary Gallery -->
    <div id="panel-gallery" class="space-y-2">
      <div class="grid grid-cols-3 gap-2">
        <div class="rounded-xl overflow-hidden border border-[var(--card-border)] relative group">
          <img src="{HERO_B64}" alt="Sanctuary studio" class="w-full h-24 object-cover">
          <span class="absolute bottom-1 left-1 bg-black/60 text-white text-[9px] px-1.5 py-0.5 rounded backdrop-blur-xs font-medium">Studio</span>
        </div>
        <div class="rounded-xl overflow-hidden border border-[var(--card-border)] relative group">
          <img src="{INSTRUCTOR_B64}" alt="Instructor pose" class="w-full h-24 object-cover">
          <span class="absolute bottom-1 left-1 bg-black/60 text-white text-[9px] px-1.5 py-0.5 rounded backdrop-blur-xs font-medium">Elena</span>
        </div>
        <div class="rounded-xl overflow-hidden border border-[var(--card-border)] relative group">
          <img src="{TEA_B64}" alt="Tea ceremony" class="w-full h-24 object-cover">
          <span class="absolute bottom-1 left-1 bg-black/60 text-white text-[9px] px-1.5 py-0.5 rounded backdrop-blur-xs font-medium">Tea Lounge</span>
        </div>
      </div>
      <p class="text-[11px] text-[var(--muted-foreground)] text-center">Light-filled sanctuary with radiant heated oak floors & living air-purifying botanicals.</p>
    </div>

    <!-- Tab 2: Curriculum -->
    <div id="panel-curriculum" class="space-y-2 hidden">
      <div class="flex gap-1 overflow-x-auto pb-1 text-[11px] font-medium">
        <button onclick="viewWeek(1)" id="w1" class="w-btn px-2 py-0.5 rounded bg-[#4A6054] text-white">W1</button>
        <button onclick="viewWeek(2)" id="w2" class="w-btn px-2 py-0.5 rounded bg-[var(--content)]/50 text-[var(--muted-foreground)]">W2</button>
        <button onclick="viewWeek(3)" id="w3" class="w-btn px-2 py-0.5 rounded bg-[var(--content)]/50 text-[var(--muted-foreground)]">W3</button>
        <button onclick="viewWeek(4)" id="w4" class="w-btn px-2 py-0.5 rounded bg-[var(--content)]/50 text-[var(--muted-foreground)]">W4</button>
        <button onclick="viewWeek(5)" id="w5" class="w-btn px-2 py-0.5 rounded bg-[var(--content)]/50 text-[var(--muted-foreground)]">W5</button>
        <button onclick="viewWeek(6)" id="w6" class="w-btn px-2 py-0.5 rounded bg-[var(--content)]/50 text-[var(--muted-foreground)]">W6</button>
      </div>

      <div class="bg-[var(--card)] border border-[var(--card-border)] rounded-xl p-2.5 text-xs space-y-1 shadow-xs">
        <div class="flex items-center justify-between">
          <strong class="text-[var(--foreground)]" id="w-title">Week 1: Awaken & Ground</strong>
          <span class="text-[10px] text-[#C87D55] font-semibold" id="w-archetype">Prithvi (Earth)</span>
        </div>
        <p class="text-[var(--muted-foreground)] leading-relaxed text-[11px]" id="w-desc">
          Anchor stability into feet, pelvic floor, and lower spine with foot-to-crown fascial unwinding.
        </p>
      </div>
    </div>

    <!-- Tab 3: Floor Plan -->
    <div id="panel-mats" class="space-y-2 hidden">
      <div class="bg-[var(--card)] border border-[var(--card-border)] p-2.5 rounded-xl text-center space-y-2">
        <div class="text-[10px] text-stone-500 font-bold uppercase tracking-wider">Guide Altar & Sound Bowls</div>
        <div class="grid grid-cols-6 gap-1 max-w-xs mx-auto text-[10px] font-bold">
          <span class="p-1 rounded bg-stone-300 text-stone-500">1</span>
          <span class="p-1 rounded bg-stone-300 text-stone-500">2</span>
          <span class="p-1 rounded bg-stone-300 text-stone-500">3</span>
          <span class="p-1 rounded bg-[#C87D55] text-white animate-pulse">4★</span>
          <span class="p-1 rounded bg-stone-300 text-stone-500">5</span>
          <span class="p-1 rounded bg-stone-300 text-stone-500">6</span>
          <span class="p-1 rounded bg-[#C87D55] text-white animate-pulse">7★</span>
          <span class="p-1 rounded bg-stone-300 text-stone-500">8</span>
          <span class="p-1 rounded bg-stone-300 text-stone-500">9</span>
          <span class="p-1 rounded bg-stone-300 text-stone-500">10</span>
          <span class="p-1 rounded bg-[#C87D55] text-white animate-pulse">11★</span>
          <span class="p-1 rounded bg-stone-300 text-stone-500">12</span>
        </div>
        <p class="text-[10px] text-[var(--muted-foreground)]">Golden mats (★) are open for reservation. 18 of 24 already filled.</p>
      </div>
    </div>

    <!-- Tab 4: Sound Healing Player -->
    <div id="panel-sound" class="space-y-2 hidden">
      <div class="bg-[var(--card)] border border-[var(--card-border)] p-3 rounded-xl flex items-center justify-between gap-3 text-xs">
        <div>
          <strong class="block text-[var(--foreground)]">432Hz Quartz Singing Bowl</strong>
          <span class="text-[10px] text-[var(--muted-foreground)]">Pure harmonic tone via Web Audio API</span>
        </div>
        <button type="button" onclick="playWidgetSound()" id="btnWidgetSound" class="bg-[#C87D55] text-white font-bold px-3 py-1.5 rounded-full hover:bg-[#B16943] transition">
          Play Tone ▶
        </button>
      </div>
    </div>

    <!-- Quick Action Footer -->
    <div class="pt-2 border-t border-[var(--card-border)] flex items-center justify-between text-xs">
      <span class="text-[11px] text-[var(--muted-foreground)]">April 6 – May 17 • Mill Valley</span>
      <span class="text-[#C87D55] font-bold">Early Bird: $339</span>
    </div>
  </div>

  <script>
    const weeks = {{
      1: {{ title: "Week 1: Awaken & Ground", archetype: "Prithvi (Earth)", desc: "Anchor stability into feet, pelvic floor, and lower spine with foot-to-crown fascial unwinding." }},
      2: {{ title: "Week 2: Fluid Detox & Mobility", archetype: "Jala (Water)", desc: "Spiraling curvilinear flows to stimulate lymphatic circulation and melt rigid winter connective tissue." }},
      3: {{ title: "Week 3: Ignite Inner Vitality", archetype: "Agni (Fire)", desc: "Activate core stamina and Manipura solar plexus warmth without crossing into frantic stress or burnout." }},
      4: {{ title: "Week 4: Heart Opening & Breath", archetype: "Anahata (Air)", desc: "Release shoulder hunching and tight pectorals with prop-supported backbends and heart coherence breathing." }},
      5: {{ title: "Week 5: Sound Alchemy & Vagus", archetype: "Akasha (Space)", desc: "Deep restorative yin postures combined with 432Hz frosted crystal singing bowls to recalibrate the vagus nerve." }},
      6: {{ title: "Week 6: Full Bloom & Integration", archetype: "Sahasrara (Crown)", desc: "Weave the six weeks into a sustainable lifelong personal home practice, ending in a celebratory tea ceremony." }}
    }};

    function setTab(name) {{
      ['gallery', 'curriculum', 'mats', 'sound'].forEach(t => {{
        document.getElementById(`panel-${{t}}`).classList.toggle('hidden', t !== name);
        const btn = document.getElementById(`btn-${{t}}`);
        if (t === name) {{
          btn.className = "py-1.5 px-2 rounded-lg bg-[var(--card)] text-[var(--foreground)] shadow-xs transition text-center";
        }} else {{
          btn.className = "py-1.5 px-2 rounded-lg text-[var(--muted-foreground)] hover:text-[var(--foreground)] transition text-center";
        }}
      }});
    }}

    function viewWeek(num) {{
      document.querySelectorAll('.w-btn').forEach((b, i) => {{
        if (i + 1 === num) {{
          b.className = "w-btn px-2 py-0.5 rounded bg-[#4A6054] text-white";
        }} else {{
          b.className = "w-btn px-2 py-0.5 rounded bg-[var(--content)]/50 text-[var(--muted-foreground)]";
        }}
      }});
      const d = weeks[num];
      if (d) {{
        document.getElementById('w-title').textContent = d.title;
        document.getElementById('w-archetype').textContent = d.archetype;
        document.getElementById('w-desc').textContent = d.desc;
      }}
    }}

    let wAudio = null;
    let wPlaying = false;
    let wOsc = null;

    function playWidgetSound() {{
      const btn = document.getElementById('btnWidgetSound');
      if (wPlaying) {{
        if (wOsc) wOsc.stop();
        if (wAudio) wAudio.close();
        wPlaying = false;
        btn.textContent = 'Play Tone ▶';
      }} else {{
        wAudio = new (window.AudioContext || window.webkitAudioContext)();
        const gain = wAudio.createGain();
        gain.gain.setValueAtTime(0.01, wAudio.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.15, wAudio.currentTime + 1);
        gain.connect(wAudio.destination);

        wOsc = wAudio.createOscillator();
        wOsc.frequency.setValueAtTime(432, wAudio.currentTime);
        wOsc.connect(gain);
        wOsc.start();
        wPlaying = true;
        btn.textContent = 'Pause ⏸';
      }}
    }}
  </script>
</body>
</html>
"""

with open(os.path.join(artifact_dir, 'bloom_room_widget.html'), 'w') as f:
    f.write(html_widget)
print("Updated bloom_room_widget.html with base64 gallery thumbnails, floor plan, and 432Hz audio.")

# Also update /home/antigravity/index.html with the base64 images so local files also have 100% visible images
with open('/home/antigravity/index.html', 'r') as f:
    idx_content = f.read()

# Replace asset references with base64
idx_content = idx_content.replace('src="assets/hero.jpg"', f'src="{HERO_B64}"')
idx_content = idx_content.replace('src="assets/instructor.jpg"', f'src="{INSTRUCTOR_B64}"')
idx_content = idx_content.replace('src="assets/ritual.jpg"', f'src="{RITUAL_B64}"')

with open('/home/antigravity/index.html', 'w') as f:
    f.write(idx_content)
print("Updated /home/antigravity/index.html with embedded base64 images.")

print("All builds completed successfully!")
