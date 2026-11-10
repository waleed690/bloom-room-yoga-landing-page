/**
 * Bloom Room Yoga — 6-Week Spring Renewal Program
 * Interactive Web Application Scripts
 */

document.addEventListener('DOMContentLoaded', () => {

  /* ==========================================================================
     1. Live Countdown Timer
     ========================================================================== */
  const countdownTimer = () => {
    // Set target date 4 days from current simulation
    const targetDate = new Date();
    targetDate.setDate(targetDate.getDate() + 4);
    targetDate.setHours(targetDate.getHours() + 14);

    const updateTimer = () => {
      const now = new Date().getTime();
      const difference = targetDate.getTime() - now;

      if (difference <= 0) return;

      const days = Math.floor(difference / (1000 * 60 * 60 * 24));
      const hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      const minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
      const seconds = Math.floor((difference % (1000 * 60)) / 1000);

      const daysEl = document.getElementById('days');
      const hoursEl = document.getElementById('hours');
      const minutesEl = document.getElementById('minutes');
      const secondsEl = document.getElementById('seconds');

      if (daysEl) daysEl.textContent = String(days).padStart(2, '0');
      if (hoursEl) hoursEl.textContent = String(hours).padStart(2, '0');
      if (minutesEl) minutesEl.textContent = String(minutes).padStart(2, '0');
      if (secondsEl) secondsEl.textContent = String(seconds).padStart(2, '0');
    };

    updateTimer();
    setInterval(updateTimer, 1000);
  };
  countdownTimer();

  /* ==========================================================================
     2. Weekly Curriculum Data & Switcher
     ========================================================================== */
  const weeksData = {
    1: {
      weekNum: "Week 1",
      archetype: "Prithvi (Earth Archetype)",
      title: "Awaken & Ground",
      desc: "Emerge from winter hibernation by anchoring stability into the feet, pelvic bowl, and lower spine. We begin with mindful fascial hydration and gentle joint unwinding to establish safe, stable roots before upward expansion.",
      physical: "Low-center-of-gravity grounding vinyasa, standing root holds, and gentle hip capsule mobility.",
      breath: "Dirga Pranayama (Three-Part Breath) with tactile lower belly awareness.",
      sound: "Warm grounding lower-octave Tibetan brass bowls and cedarwood essential mist.",
      gift: "Bloom Room Natural Cork Fascial Sphere for home foot and sacrum unwinding.",
      prompt: "Where in my body and life am I still carrying winter heaviness, and what foundation am I ready to build upon?",
      practices: [
        "Foot & Ankle Fascial Awakening",
        "Slow Grounding Vinyasa (Root Chakra)",
        "Nervous System Orienting Exercise",
        "Introduction to the Seasonal Journal"
      ]
    },
    2: {
      weekNum: "Week 2",
      archetype: "Jala (Water Archetype)",
      title: "Fluid Mobility & Detox",
      desc: "Encourage natural lymphatic circulation and spinal decompression through spiraling, organic flows. Rather than rigid angles, Week 2 explores curvilinear movement to lubricate synovial joints and melt stagnant connective tissue.",
      physical: "Spiral pelvic sways, rhythmic sun salutations, thoracic rotation, and restorative side-body lengthening.",
      breath: "Nadi Shodhana (Alternate Nostril Breathing) to harmonize brain hemispheres.",
      sound: "Flowing koshi wind chimes and tuned crystal bowls evoking river currents.",
      gift: "Organic botanical dandelion & lemongrass spring lymphatic tea blend.",
      prompt: "Where am I gripping or resisting natural change, and how can I bring more fluid adaptability to my days?",
      practices: [
        "Lymphatic Pump Flow & Gentle Inversions",
        "Spinal Wave Decompression",
        "Hydration & Spring Herbology Circle",
        "Evening Candlelit Hip Opening"
      ]
    },
    3: {
      weekNum: "Week 3",
      archetype: "Agni (Fire Archetype)",
      title: "Ignite Vitality & Inner Sun",
      desc: "Kindle the transformative internal fire of the solar plexus (Manipura). Build lean physical stamina, core buoyancy, and focused determination without tipping into frantic exhaustion or nervous burnout.",
      physical: "Dynamic standing balance series, solar vinyasa pacing, intelligent core integration, and warrior expansions.",
      breath: "Kapalabhati (Skull-Shining Breath) followed by Kumbhaka retention practice.",
      sound: "Resonant brass gongs and solar quartz crystal tones.",
      gift: "Aromatherapy Solar Roll-On: ginger, bergamot & sweet orange.",
      prompt: "What creative spark or healthy habit is ready to be fed with steady, disciplined enthusiasm?",
      practices: [
        "Core Center & Psoas Awareness",
        "Power & Grace Balance Transitions",
        "Digestive Health & Agni Lecture",
        "Twilight Cooling Yin Counterbalance"
      ]
    },
    4: {
      weekNum: "Week 4",
      archetype: "Anahata (Heart & Air Archetype)",
      title: "Heart Opening & Spacious Breath",
      desc: "Release habitual protective hunching, tight pectorals, and shallow upper-chest breathing. Cultivate expansive shoulder mobility, supported gentle backbends, and compassionate emotional availability.",
      physical: "Bolster-supported fish pose, camel pose variations, prone cobra waves, and shoulder flossing.",
      breath: "Anahata heart coherence breathing with 5.5-second rhythm.",
      sound: "528Hz crystal singing bowl known for heart resonance.",
      gift: "Handmade organic linen lavender eye pillow for savasana.",
      prompt: "What armor around my heart am I safe to soften now, and what compassion can I extend toward myself?",
      practices: [
        "Shoulder Girdle & Upper Spine Unwinding",
        "Supported Backbend Exploration",
        "Metta (Loving-Kindness) Meditation",
        "Post-Class Herbal Rose Tisane Tasting"
      ]
    },
    5: {
      weekNum: "Week 5",
      archetype: "Akasha (Space & Sound Archetype)",
      title: "Sound Alchemy & Vagus Release",
      desc: "Delve into the quietest, most subtle layer of restoration. We explore restorative yoga postures held for 6–10 minutes with full prop support, combined with a therapeutic sound bath to stimulate the vagus nerve.",
      physical: "Supported floor yin postures, legs-up-the-wall inversion, and neck somatic de-armoring.",
      breath: "Bhramari (Humming Bee Breath) to tone the vagal pathways.",
      sound: "Complete 432Hz frosted quartz singing bowl sound bath immersion.",
      gift: "Bloom Room Ceremonial Palo Santo & Jasmine Room Mist.",
      prompt: "In the spacious quiet between my thoughts, what gentle wisdom is waiting to be heard?",
      practices: [
        "90-Minute Restorative Yin Sanctuary",
        "Therapeutic Sound Immersion Experience",
        "Vagus Nerve & Autonomic Health Education",
        "Silent Walking Meditation in the Garden"
      ]
    },
    6: {
      weekNum: "Week 6",
      archetype: "Sahasrara (Full Bloom Archetype)",
      title: "Full Bloom & Integration",
      desc: "Celebrate six weeks of dedicated seasonal transformation. Consolidate your physical strength, renewed vitality, and mental peace into an enduring sustainable personal home practice for the rest of the year.",
      physical: "Graceful celebratory flow weaving together elements of all previous weeks, followed by deep savasana.",
      breath: "Sama Vritti (Equal Ratio Breath) and effortless open-awareness meditation.",
      sound: "Harmonic choir of singing bowls, acoustic chime bells, and closing singing bowl circle.",
      gift: "Hand-thrown ceramic Bloom Room tea cup and personalized cohort diploma.",
      prompt: "Who have I grown into over these six weeks, and how will I carry this calm radiance into the world?",
      practices: [
        "Integration Masterclass (All Faculty)",
        "Building Your 15-Minute Home Ritual",
        "Cohort Closing Ceremony & Cacao Tasting",
        "Alumni Community Circle Access"
      ]
    }
  };

  const renderCurriculum = (weekNum) => {
    const data = weeksData[weekNum];
    if (!data) return;

    const cardContainer = document.getElementById('curriculumCard');
    if (!cardContainer) return;

    cardContainer.innerHTML = `
      <div class="curriculum-content-left">
        <span class="curriculum-week-badge">${data.weekNum} • ${data.archetype}</span>
        <h3 class="curriculum-title">${data.title}</h3>
        <p class="curriculum-desc">${data.desc}</p>

        <div class="curriculum-details-grid">
          <div class="detail-block">
            <strong>Movement Practice</strong>
            <p>${data.physical}</p>
          </div>
          <div class="detail-block">
            <strong>Breath & Stillness</strong>
            <p>${data.breath}</p>
          </div>
          <div class="detail-block">
            <strong>Sensory Soundscape</strong>
            <p>${data.sound}</p>
          </div>
          <div class="detail-block">
            <strong>Weekly Ritual Gift</strong>
            <p>${data.gift}</p>
          </div>
        </div>

        <div class="curriculum-journal-prompt">
          <strong>Weekly Journal Inquiry:</strong>
          <p>"${data.prompt}"</p>
        </div>
      </div>

      <div class="curriculum-visual-right">
        <h4>Key Focus Sessions This Week</h4>
        <ul class="curriculum-bullet-list">
          ${data.practices.map(p => `
            <li>
              <span class="bullet-icon">✦</span>
              <span>${p}</span>
            </li>
          `).join('')}
        </ul>

        <div style="margin-top: 12px; border-top: 1px solid var(--color-border); padding-top: 16px;">
          <button type="button" class="btn btn-primary btn-block btn-curriculum-reserve" data-week="${weekNum}">
            Reserve for Spring Cohort
          </button>
        </div>
      </div>
    `;

    // Attach click to the newly created button
    const reserveBtn = cardContainer.querySelector('.btn-curriculum-reserve');
    if (reserveBtn) {
      reserveBtn.addEventListener('click', () => {
        openModal();
      });
    }
  };

  // Initialize Week 1
  renderCurriculum(1);

  // Tab click handler
  const weekTabButtons = document.querySelectorAll('.week-tab');
  weekTabButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      weekTabButtons.forEach(b => {
        b.classList.remove('active');
        b.setAttribute('aria-selected', 'false');
      });
      btn.classList.add('active');
      btn.setAttribute('aria-selected', 'true');
      const week = btn.getAttribute('data-week');
      renderCurriculum(week);
    });
  });

  /* ==========================================================================
     3. Interactive Spring Renewal Quiz
     ========================================================================== */
  const quizState = {
    feeling: '',
    experience: '',
    timePreference: ''
  };

  const quizStep1 = document.getElementById('quizStep1');
  const quizStep2 = document.getElementById('quizStep2');
  const quizStep3 = document.getElementById('quizStep3');
  const quizResult = document.getElementById('quizResult');

  // Step 1 Options
  if (quizStep1) {
    quizStep1.querySelectorAll('.quiz-option').forEach(btn => {
      btn.addEventListener('click', () => {
        quizState.feeling = btn.getAttribute('data-ans');
        quizStep1.classList.remove('active');
        quizStep2.classList.add('active');
      });
    });
  }

  // Step 2 Options
  if (quizStep2) {
    quizStep2.querySelectorAll('.quiz-option').forEach(btn => {
      btn.addEventListener('click', () => {
        quizState.experience = btn.getAttribute('data-ans');
        quizStep2.classList.remove('active');
        quizStep3.classList.add('active');
      });
    });
  }

  // Step 3 Options
  if (quizStep3) {
    quizStep3.querySelectorAll('.quiz-option').forEach(btn => {
      btn.addEventListener('click', () => {
        quizState.timePreference = btn.getAttribute('data-ans');
        quizStep3.classList.remove('active');
        showQuizResult();
      });
    });
  }

  const showQuizResult = () => {
    if (!quizResult) return;
    quizResult.style.display = 'block';

    const resultTitle = document.getElementById('resultTitle');
    const resultSummary = document.getElementById('resultSummary');
    const recRhythm = document.getElementById('recRhythm');
    const recHerb = document.getElementById('recHerb');
    const recTier = document.getElementById('recTier');

    if (quizState.feeling === 'stiff') {
      resultTitle.textContent = 'The Fascial Mobility & Spring Awakening Track';
      resultSummary.textContent = 'Your connective tissues are primed to shed winter tightness through dynamic spiral vinyasa and deep structural hip/spine opening.';
      recRhythm.textContent = '2 Morning Solar Vinyasa + 1 Midday Fascial Decompression session weekly';
      recHerb.textContent = 'Organic meadowsweet, turmeric, and ginger circulation tonic';
      recTier.textContent = 'The Full Bloom ($439) — Includes physical cork roller box & 1:1 consult';
    } else if (quizState.feeling === 'stressed') {
      resultTitle.textContent = 'The Nervous System Restoration & Sound Path';
      resultSummary.textContent = 'Your mind and adrenals are asking for deep parasympathetic tone, silent space, and sound resonance to dissolve cumulative fatigue.';
      recRhythm.textContent = '2 Twilight Restorative Yin & Sound Alchemy + 1 Weekend Immersion';
      recHerb.textContent = 'Organic passionflower, holy basil (tulsi), and chamomile blossom elixir';
      recTier.textContent = 'The Full Bloom ($439) — Includes 2 Saturday Candlelight Sound Baths';
    } else {
      resultTitle.textContent = 'The Vitality, Balance & Inner Sun Track';
      resultSummary.textContent = 'You have a healthy foundation and are eager to tap into radiant creative stamina and steady, mindful core strength this season.';
      recRhythm.textContent = '3 Mixed Morning Solar & Evening Yin sessions weekly';
      recHerb.textContent = 'Gotu kola, ceremonial grade matcha, and lemon verbena infusion';
      recTier.textContent = 'Sanctuary Rhythm ($339) or The Full Bloom ($439)';
    }
  };

  // Retake Quiz
  const btnRestartQuiz = document.getElementById('btnRestartQuiz');
  if (btnRestartQuiz) {
    btnRestartQuiz.addEventListener('click', () => {
      quizResult.style.display = 'none';
      quizStep1.classList.add('active');
      quizState.feeling = '';
      quizState.experience = '';
      quizState.timePreference = '';
    });
  }

  // Apply Quiz Result to Modal
  const btnApplyQuizPlan = document.getElementById('btnApplyQuizPlan');
  if (btnApplyQuizPlan) {
    btnApplyQuizPlan.addEventListener('click', () => {
      openModal();
      const tierSelect = document.getElementById('selectedTier');
      const timeSelect = document.getElementById('selectedTime');

      if (quizState.feeling === 'stressed' && tierSelect) {
        tierSelect.value = 'The Full Bloom ($439)';
      }
      if (quizState.timePreference === 'morning' && timeSelect) {
        timeSelect.value = 'Morning Solar (Mon/Wed 7:00 AM)';
      } else if (quizState.timePreference === 'evening' && timeSelect) {
        timeSelect.value = 'Twilight Yin & Sound (Mon/Thu 6:30 PM)';
      }
    });
  }

  /* ==========================================================================
     4. Schedule Filter Tabs
     ========================================================================== */
  const filterBtns = document.querySelectorAll('.filter-btn');
  const scheduleCards = document.querySelectorAll('.schedule-card');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filter = btn.getAttribute('data-filter');

      scheduleCards.forEach(card => {
        if (filter === 'all' || card.getAttribute('data-time') === filter) {
          card.style.display = 'block';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });

  /* ==========================================================================
     5. Pricing Upfront vs. Installments Switch
     ========================================================================== */
  const pricingToggle = document.getElementById('pricingToggle');
  let isSplitPayment = false;

  if (pricingToggle) {
    pricingToggle.addEventListener('click', () => {
      isSplitPayment = !isSplitPayment;
      pricingToggle.classList.toggle('active', isSplitPayment);
      pricingToggle.setAttribute('aria-checked', String(isSplitPayment));

      const priceAmounts = document.querySelectorAll('.price-amount');
      const pricePeriods = document.querySelectorAll('.price-period');

      priceAmounts.forEach(amt => {
        const full = amt.getAttribute('data-full');
        const split = amt.getAttribute('data-split');
        amt.textContent = isSplitPayment ? split : full;
      });

      pricePeriods.forEach(period => {
        const fullText = period.getAttribute('data-full');
        const splitText = period.getAttribute('data-split');
        period.textContent = isSplitPayment ? splitText : fullText;
      });
    });
  }

  /* ==========================================================================
     6. Booking Modal Logic
     ========================================================================== */
  const modal = document.getElementById('bookingModal');
  const modalClose = document.getElementById('modalClose');
  const modalStep1 = document.getElementById('modalStep1');
  const modalStep2 = document.getElementById('modalStep2');
  const reservationForm = document.getElementById('reservationForm');
  const btnCloseConfirm = document.getElementById('btnCloseConfirm');

  const openModal = (preselectedTier) => {
    if (!modal) return;
    modal.classList.add('open');
    modal.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';

    if (modalStep1) modalStep1.style.display = 'block';
    if (modalStep2) modalStep2.style.display = 'none';

    if (preselectedTier) {
      const tierSelect = document.getElementById('selectedTier');
      if (tierSelect) {
        for (let i = 0; i < tierSelect.options.length; i++) {
          if (tierSelect.options[i].value.includes(preselectedTier)) {
            tierSelect.selectedIndex = i;
            break;
          }
        }
      }
    }
  };

  const closeModal = () => {
    if (!modal) return;
    modal.classList.remove('open');
    modal.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  };

  if (modalClose) modalClose.addEventListener('click', closeModal);
  if (btnCloseConfirm) btnCloseConfirm.addEventListener('click', closeModal);

  // Close when clicking outside modal box
  if (modal) {
    modal.addEventListener('click', (e) => {
      if (e.target === modal) {
        closeModal();
      }
    });
  }

  // Trigger buttons across page
  const reserveButtons = [
    document.getElementById('btnNavReserve'),
    document.getElementById('btnHeroReserve'),
    document.getElementById('btnMobileReserve'),
    document.getElementById('btnFinalReserve')
  ];

  reserveButtons.forEach(btn => {
    if (btn) btn.addEventListener('click', () => openModal());
  });

  // Quiz trigger in nav
  const btnOpenQuiz = document.getElementById('btnOpenQuiz');
  if (btnOpenQuiz) {
    btnOpenQuiz.addEventListener('click', () => {
      const quizSection = document.getElementById('quiz');
      if (quizSection) quizSection.scrollIntoView({ behavior: 'smooth' });
    });
  }

  // Tier selection buttons
  const tierButtons = document.querySelectorAll('.btn-select-tier');
  tierButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const tierName = btn.getAttribute('data-tier');
      openModal(tierName);
    });
  });

  // Reservation Form Submit Handler
  if (reservationForm) {
    reservationForm.addEventListener('submit', (e) => {
      e.preventDefault();

      const fName = document.getElementById('custFirstName').value;
      const lName = document.getElementById('custLastName').value;
      const email = document.getElementById('custEmail').value;
      const tier = document.getElementById('selectedTier').value;
      const cadence = document.getElementById('selectedTime').value;

      // Populate confirmation screen
      const sumName = document.getElementById('sumName');
      const sumTier = document.getElementById('sumTier');
      const sumCadence = document.getElementById('sumCadence');
      const sumEmail = document.getElementById('sumEmail');

      if (sumName) sumName.textContent = `${fName} ${lName}`;
      if (sumTier) sumTier.textContent = tier;
      if (sumCadence) sumCadence.textContent = cadence;
      if (sumEmail) sumEmail.textContent = email;

      modalStep1.style.display = 'none';
      modalStep2.style.display = 'block';
    });
  }

  // Download Calendar (.ics)
  const btnDownloadCal = document.getElementById('btnDownloadCal');
  if (btnDownloadCal) {
    btnDownloadCal.addEventListener('click', () => {
      const icsData = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Bloom Room Yoga//Spring Renewal 2026//EN",
        "BEGIN:VEVENT",
        "UID:bloom-renewal-2026@bloomroomyoga.com",
        "DTSTAMP:20260406T070000Z",
        "DTSTART:20260406T140000Z",
        "DTEND:20260406T151500Z",
        "SUMMARY:Bloom Room — 6-Week Spring Renewal Orientation & First Practice",
        "DESCRIPTION:Welcome to the 6-Week Spring Renewal Program at Bloom Room Sanctuary.",
        "LOCATION:Bloom Room Sanctuary, 428 Blossom Way, Mill Valley CA",
        "STATUS:CONFIRMED",
        "END:VEVENT",
        "END:VCALENDAR"
      ].join("\r\n");

      const blob = new Blob([icsData], { type: "text/calendar;charset=utf-8" });
      const link = document.createElement("a");
      link.href = window.URL.createObjectURL(blob);
      link.setAttribute("download", "bloom_room_spring_renewal.ics");
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    });
  }

  /* ==========================================================================
     7. FAQ Accordion Toggle
     ========================================================================== */
  const faqItems = document.querySelectorAll('.faq-item');

  faqItems.forEach(item => {
    const questionBtn = item.querySelector('.faq-question');
    const answer = item.querySelector('.faq-answer');

    if (questionBtn && answer) {
      questionBtn.addEventListener('click', () => {
        const isActive = item.classList.contains('active');

        // Close all other items
        faqItems.forEach(otherItem => {
          if (otherItem !== item) {
            otherItem.classList.remove('active');
            otherItem.querySelector('.faq-question').setAttribute('aria-expanded', 'false');
            otherItem.querySelector('.faq-answer').style.maxHeight = null;
          }
        });

        // Toggle clicked item
        if (isActive) {
          item.classList.remove('active');
          questionBtn.setAttribute('aria-expanded', 'false');
          answer.style.maxHeight = null;
        } else {
          item.classList.add('active');
          questionBtn.setAttribute('aria-expanded', 'true');
          answer.style.maxHeight = answer.scrollHeight + 40 + 'px';
        }
      });
    }
  });

  /* ==========================================================================
     8. Mobile Navigation Drawer Toggle
     ========================================================================== */
  const mobileToggle = document.getElementById('mobileToggle');
  const mobileDrawer = document.getElementById('mobileDrawer');

  if (mobileToggle && mobileDrawer) {
    mobileToggle.addEventListener('click', () => {
      const isVisible = mobileDrawer.style.display === 'block';
      mobileDrawer.style.display = isVisible ? 'none' : 'block';
    });

    const mobileLinks = mobileDrawer.querySelectorAll('.mobile-link');
    mobileLinks.forEach(link => {
      link.addEventListener('click', () => {
        mobileDrawer.style.display = 'none';
      });
    });
  }

  /* ==========================================================================
     9. Newsletter Subscription Feedback
     ========================================================================== */
  const newsletterForm = document.getElementById('newsletterForm');
  const newsNotice = document.getElementById('newsNotice');
  const newsEmail = document.getElementById('newsEmail');

  if (newsletterForm && newsNotice) {
    newsletterForm.addEventListener('submit', (e) => {
      e.preventDefault();
      if (newsEmail && newsEmail.value) {
        newsletterForm.style.display = 'none';
        newsNotice.style.display = 'block';
      }
    });
  }

});
