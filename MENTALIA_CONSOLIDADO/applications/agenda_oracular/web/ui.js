// ORÁCULO MENTALIA - UI JavaScript
// Sistema de onboarding RUT Astral y funcionalidades interactivas

// Estado global de la aplicación
const appState = {
    currentStep: 1,
    totalSteps: 4,
    formData: {},
    selectedNeurotypes: [],
    calculatedProfile: null
};

// Datos de ejemplo para eventos oraculares
const sampleEvents = [
    {
        date: "2025-08-15",
        title: "Luna Llena en Acuario",
        arcano: "La Estrella",
        description: "Momento ideal para liberación emocional y visión futura",
        color: "AZUL",
        microaction: "Escribe 3 deseos bajo la luna llena"
    },
    {
        date: "2025-08-22",
        title: "Portal 8·22 · Abundancia",
        arcano: "El Emperador",
        description: "Energía de manifestación material y estructura",
        color: "VERDE",
        microaction: "Organiza tus finanzas y establece metas claras"
    },
    {
        date: "2025-09-01",
        title: "Nueva Luna en Virgo",
        arcano: "El Ermitaño",
        description: "Tiempo de introspección y perfeccionamiento personal",
        color: "VIOLETA",
        microaction: "Inicia un nuevo hábito de autocuidado"
    }
];

// Inicialización de la aplicación
document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
    setupEventListeners();
    setupNeurotypeSelection();
    setupTimeEstimator();
});

function initializeApp() {
    console.log('🔮 ORÁCULO MENTALIA - Inicializando aplicación');
    updateProgressBar();
}

function setupEventListeners() {
    // Event listeners para navegación de formulario
    const nextBtn = document.getElementById('nextBtn');
    const prevBtn = document.getElementById('prevBtn');
    const submitBtn = document.getElementById('submitBtn');
    
    if (nextBtn) nextBtn.addEventListener('click', nextStep);
    if (prevBtn) prevBtn.addEventListener('click', previousStep);
    if (submitBtn) submitBtn.addEventListener('click', submitForm);
    
    // Event listeners para campos de formulario
    setupFormValidation();
}

function setupNeurotypeSelection() {
    const neurotypeCards = document.querySelectorAll('.neurotype-card');
    
    neurotypeCards.forEach(card => {
        card.addEventListener('click', function() {
            const neurotype = this.dataset.neurotype;
            toggleNeurotypeSelection(this, neurotype);
        });
    });
}

function toggleNeurotypeSelection(card, neurotype) {
    const isSelected = card.classList.contains('selected');
    
    if (isSelected) {
        card.classList.remove('selected');
        appState.selectedNeurotypes = appState.selectedNeurotypes.filter(n => n !== neurotype);
    } else {
        card.classList.add('selected');
        if (!appState.selectedNeurotypes.includes(neurotype)) {
            appState.selectedNeurotypes.push(neurotype);
        }
    }
    
    console.log('Neurotipos seleccionados:', appState.selectedNeurotypes);
}

function setupTimeEstimator() {
    const precisionSelect = document.getElementById('precisionHora');
    const timeEstimator = document.getElementById('timeEstimator');
    
    if (precisionSelect) {
        precisionSelect.addEventListener('change', function() {
            if (this.value === 'desconocida') {
                timeEstimator.style.display = 'block';
            } else {
                timeEstimator.style.display = 'none';
            }
        });
    }
}

function setupFormValidation() {
    // Validación en tiempo real para campos requeridos
    const requiredFields = document.querySelectorAll('input[required], select[required]');
    
    requiredFields.forEach(field => {
        field.addEventListener('blur', validateField);
        field.addEventListener('input', clearFieldError);
    });
}

function validateField(event) {
    const field = event.target;
    const value = field.value.trim();
    
    if (!value) {
        showFieldError(field, 'Este campo es requerido');
        return false;
    }
    
    // Validaciones específicas por tipo
    if (field.type === 'email' && !isValidEmail(value)) {
        showFieldError(field, 'Ingresa un email válido');
        return false;
    }
    
    clearFieldError(field);
    return true;
}

function showFieldError(field, message) {
    clearFieldError(field);
    
    const errorDiv = document.createElement('div');
    errorDiv.className = 'field-error';
    errorDiv.textContent = message;
    errorDiv.style.color = 'var(--oracle-red)';
    errorDiv.style.fontSize = '0.75rem';
    errorDiv.style.marginTop = 'var(--spacing-xs)';
    
    field.parentNode.appendChild(errorDiv);
    field.style.borderColor = 'var(--oracle-red)';
}

function clearFieldError(field) {
    const errorDiv = field.parentNode.querySelector('.field-error');
    if (errorDiv) {
        errorDiv.remove();
    }
    field.style.borderColor = '';
}

function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// Funciones de navegación del formulario
function startOnboarding() {
    document.getElementById('welcome').classList.add('hidden');
    document.getElementById('onboarding').classList.remove('hidden');
    appState.currentStep = 1;
    updateProgressBar();
    showStep(1);
}

function nextStep() {
    if (validateCurrentStep()) {
        saveCurrentStepData();
        
        if (appState.currentStep < appState.totalSteps) {
            appState.currentStep++;
            showStep(appState.currentStep);
            updateProgressBar();
            updateNavigationButtons();
        }
    }
}

function previousStep() {
    if (appState.currentStep > 1) {
        appState.currentStep--;
        showStep(appState.currentStep);
        updateProgressBar();
        updateNavigationButtons();
    }
}

function showStep(stepNumber) {
    // Ocultar todos los pasos
    document.querySelectorAll('.form-step').forEach(step => {
        step.classList.remove('active');
    });
    
    // Mostrar el paso actual
    const currentStep = document.getElementById(`step${stepNumber}`);
    if (currentStep) {
        currentStep.classList.add('active');
    }
}

function updateProgressBar() {
    const progressFill = document.getElementById('progressFill');
    const progressText = document.getElementById('progressText');
    
    const percentage = (appState.currentStep / appState.totalSteps) * 100;
    
    if (progressFill) {
        progressFill.style.width = `${percentage}%`;
    }
    
    if (progressText) {
        progressText.textContent = `Paso ${appState.currentStep} de ${appState.totalSteps}`;
    }
}

function updateNavigationButtons() {
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const submitBtn = document.getElementById('submitBtn');
    
    // Mostrar/ocultar botón anterior
    if (prevBtn) {
        prevBtn.style.display = appState.currentStep > 1 ? 'inline-flex' : 'none';
    }
    
    // Mostrar botón siguiente o enviar
    if (appState.currentStep === appState.totalSteps) {
        if (nextBtn) nextBtn.style.display = 'none';
        if (submitBtn) submitBtn.style.display = 'inline-flex';
    } else {
        if (nextBtn) nextBtn.style.display = 'inline-flex';
        if (submitBtn) submitBtn.style.display = 'none';
    }
}

function validateCurrentStep() {
    const currentStepElement = document.getElementById(`step${appState.currentStep}`);
    const requiredFields = currentStepElement.querySelectorAll('input[required], select[required]');
    
    let isValid = true;
    
    requiredFields.forEach(field => {
        if (!validateField({ target: field })) {
            isValid = false;
        }
    });
    
    // Validaciones específicas por paso
    switch (appState.currentStep) {
        case 3:
            if (appState.selectedNeurotypes.length === 0) {
                showNotification('Por favor selecciona al menos un neurotipo', 'warning');
                isValid = false;
            }
            break;
        case 4:
            const consentDatos = document.getElementById('consentDatos');
            if (!consentDatos.checked) {
                showNotification('Debes aceptar el uso de datos astrológicos para continuar', 'error');
                isValid = false;
            }
            break;
    }
    
    return isValid;
}

function saveCurrentStepData() {
    const currentStepElement = document.getElementById(`step${appState.currentStep}`);
    const formFields = currentStepElement.querySelectorAll('input, select, textarea');
    
    formFields.forEach(field => {
        if (field.type === 'checkbox') {
            appState.formData[field.id] = field.checked;
        } else {
            appState.formData[field.id] = field.value;
        }
    });
    
    // Guardar neurotipos seleccionados
    if (appState.currentStep === 3) {
        appState.formData.neurotipos = [...appState.selectedNeurotypes];
    }
    
    console.log('Datos guardados del paso', appState.currentStep, ':', appState.formData);
}

// Funciones de cálculo astrológico
function estimateTime() {
    const ritmo = document.getElementById('ritmoCircadiano').value;
    const personalidad = document.getElementById('personalidad').value;
    
    if (!ritmo || !personalidad) {
        showNotification('Por favor responde ambas preguntas para estimar la hora', 'warning');
        return;
    }
    
    let estimatedHour = 12; // Hora base: mediodía
    
    // Ajustar según ritmo circadiano
    switch (ritmo) {
        case 'manana':
            estimatedHour -= 4; // 8:00 AM
            break;
        case 'tarde':
            estimatedHour += 6; // 6:00 PM
            break;
        case 'mixto':
            estimatedHour += 2; // 2:00 PM
            break;
    }
    
    // Ajustar según personalidad
    switch (personalidad) {
        case 'extrovertido':
            estimatedHour += 1;
            break;
        case 'introvertido':
            estimatedHour -= 1;
            break;
    }
    
    // Asegurar que esté en rango válido
    estimatedHour = Math.max(0, Math.min(23, estimatedHour));
    
    const timeString = `${estimatedHour.toString().padStart(2, '0')}:00`;
    document.getElementById('horaNacimiento').value = timeString;
    document.getElementById('precisionHora').value = 'estimada';
    
    showNotification(`Hora estimada: ${timeString}. Puedes ajustarla si lo deseas.`, 'success');
}

function calculateNumerology(birthDate, fullName) {
    const numerology = {};
    
    // Calcular número de vida
    const dateNumbers = birthDate.replace(/-/g, '').split('').map(Number);
    let lifeNumber = dateNumbers.reduce((sum, num) => sum + num, 0);
    while (lifeNumber > 9) {
        lifeNumber = lifeNumber.toString().split('').map(Number).reduce((sum, num) => sum + num, 0);
    }
    numerology.numeroVida = lifeNumber;
    
    // Calcular año personal (para 2025)
    const currentYear = 2025;
    const birthMonth = parseInt(birthDate.split('-')[1]);
    const birthDay = parseInt(birthDate.split('-')[2]);
    
    let personalYear = currentYear + birthMonth + birthDay;
    while (personalYear > 9) {
        personalYear = personalYear.toString().split('').map(Number).reduce((sum, num) => sum + num, 0);
    }
    numerology.numeroPersonalAnual = personalYear;
    
    // Calcular número de destino (simplificado)
    const nameValue = fullName.toLowerCase().replace(/[^a-z]/g, '').split('').reduce((sum, char) => {
        return sum + (char.charCodeAt(0) - 96);
    }, 0);
    
    let destinyNumber = nameValue;
    while (destinyNumber > 9) {
        destinyNumber = destinyNumber.toString().split('').map(Number).reduce((sum, num) => sum + num, 0);
    }
    numerology.numeroDestino = destinyNumber;
    
    return numerology;
}

function calculateAstrology(birthDate, birthTime, birthPlace) {
    // Simulación de cálculo astrológico (en producción se usaría una API real)
    const month = parseInt(birthDate.split('-')[1]);
    const day = parseInt(birthDate.split('-')[2]);
    
    const astrology = {
        signoSolar: getZodiacSign(month, day),
        signoLunar: getRandomSign(), // Simplificado
        ascendente: getRandomSign() // Simplificado
    };
    
    return astrology;
}

function getZodiacSign(month, day) {
    const signs = [
        { name: 'Capricornio', start: [12, 22], end: [1, 19] },
        { name: 'Acuario', start: [1, 20], end: [2, 18] },
        { name: 'Piscis', start: [2, 19], end: [3, 20] },
        { name: 'Aries', start: [3, 21], end: [4, 19] },
        { name: 'Tauro', start: [4, 20], end: [5, 20] },
        { name: 'Géminis', start: [5, 21], end: [6, 20] },
        { name: 'Cáncer', start: [6, 21], end: [7, 22] },
        { name: 'Leo', start: [7, 23], end: [8, 22] },
        { name: 'Virgo', start: [8, 23], end: [9, 22] },
        { name: 'Libra', start: [9, 23], end: [10, 22] },
        { name: 'Escorpio', start: [10, 23], end: [11, 21] },
        { name: 'Sagitario', start: [11, 22], end: [12, 21] }
    ];
    
    for (const sign of signs) {
        const [startMonth, startDay] = sign.start;
        const [endMonth, endDay] = sign.end;
        
        if ((month === startMonth && day >= startDay) || 
            (month === endMonth && day <= endDay)) {
            return sign.name;
        }
    }
    
    return 'Capricornio'; // Fallback
}

function getRandomSign() {
    const signs = ['Aries', 'Tauro', 'Géminis', 'Cáncer', 'Leo', 'Virgo', 
                   'Libra', 'Escorpio', 'Sagitario', 'Capricornio', 'Acuario', 'Piscis'];
    return signs[Math.floor(Math.random() * signs.length)];
}

// Función principal de envío del formulario
async function submitForm() {
    if (!validateCurrentStep()) {
        return;
    }
    
    saveCurrentStepData();
    
    // Mostrar loading
    showLoading();
    
    try {
        // Simular procesamiento (en producción sería una llamada a la API)
        await new Promise(resolve => setTimeout(resolve, 3000));
        
        // Calcular perfil
        const profile = calculateProfile();
        appState.calculatedProfile = profile;
        
        // Mostrar resultados
        hideLoading();
        showResults(profile);
        
    } catch (error) {
        hideLoading();
        showNotification('Error al procesar tu RUT Astral. Inténtalo nuevamente.', 'error');
        console.error('Error:', error);
    }
}

function calculateProfile() {
    const formData = appState.formData;
    
    // Calcular numerología
    const numerology = calculateNumerology(formData.fechaNacimiento, formData.nombreCompleto);
    
    // Calcular astrología
    const astrology = calculateAstrology(
        formData.fechaNacimiento, 
        formData.horaNacimiento, 
        formData.ciudadNacimiento
    );
    
    // Generar eventos personalizados basados en el perfil
    const personalizedEvents = generatePersonalizedEvents(numerology, astrology, appState.selectedNeurotypes);
    
    return {
        numerology,
        astrology,
        events: personalizedEvents,
        neurotypes: appState.selectedNeurotypes,
        preferences: {
            comunicacion: formData.estiloComunicacion,
            frecuencia: formData.frecuenciaConsultas
        }
    };
}

function generatePersonalizedEvents(numerology, astrology, neurotypes) {
    // Personalizar eventos basados en el perfil
    const personalizedEvents = sampleEvents.map(event => {
        const personalizedEvent = { ...event };
        
        // Adaptar microacciones según neurotipos
        if (neurotypes.includes('TDAH')) {
            personalizedEvent.microaction = adaptForTDAH(event.microaction);
        }
        
        if (neurotypes.includes('Autismo')) {
            personalizedEvent.microaction = adaptForAutism(event.microaction);
        }
        
        if (neurotypes.includes('Altas_Capacidades')) {
            personalizedEvent.microaction = adaptForGiftedness(event.microaction);
        }
        
        return personalizedEvent;
    });
    
    return personalizedEvents;
}

function adaptForTDAH(microaction) {
    return `${microaction} (Usa timer de 15 min y recompénsate al terminar)`;
}

function adaptForAutism(microaction) {
    return `${microaction} (Prepara el espacio con anticipación y sigue la rutina)`;
}

function adaptForGiftedness(microaction) {
    return `${microaction} (Conecta con patrones más amplios y documenta insights)`;
}

function showResults(profile) {
    // Ocultar onboarding y mostrar resultados
    document.getElementById('onboarding').classList.add('hidden');
    document.getElementById('results').classList.remove('hidden');
    
    // Poblar datos astrológicos
    document.getElementById('signoSolar').textContent = profile.astrology.signoSolar;
    document.getElementById('signoLunar').textContent = profile.astrology.signoLunar;
    document.getElementById('ascendente').textContent = profile.astrology.ascendente;
    
    // Poblar numerología
    document.getElementById('numeroVida').textContent = profile.numerology.numeroVida;
    document.getElementById('numeroAnual').textContent = profile.numerology.numeroPersonalAnual;
    
    // Poblar eventos
    const eventsContainer = document.getElementById('proximosEventos');
    eventsContainer.innerHTML = '';
    
    profile.events.forEach(event => {
        const eventElement = createEventElement(event);
        eventsContainer.appendChild(eventElement);
    });
    
    // Scroll to top
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function createEventElement(event) {
    const eventDiv = document.createElement('div');
    eventDiv.className = 'event-item';
    
    eventDiv.innerHTML = `
        <div class="event-date">${formatDate(event.date)}</div>
        <div class="event-details">
            <div class="event-title">${event.title}</div>
            <div class="event-description">${event.description}</div>
            <div class="event-microaction" style="font-style: italic; color: var(--oracle-gold); margin-top: var(--spacing-xs);">
                💫 ${event.microaction}
            </div>
        </div>
    `;
    
    return eventDiv;
}

function formatDate(dateString) {
    const date = new Date(dateString);
    const options = { month: 'short', day: 'numeric' };
    return date.toLocaleDateString('es-ES', options);
}

// Funciones de utilidad
function showLoading() {
    document.getElementById('loadingOverlay').classList.remove('hidden');
}

function hideLoading() {
    document.getElementById('loadingOverlay').classList.add('hidden');
}

function showNotification(message, type = 'info') {
    // Crear elemento de notificación
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: var(--spacing-md) var(--spacing-lg);
        border-radius: var(--radius-md);
        color: white;
        font-weight: 500;
        z-index: 1001;
        max-width: 400px;
        animation: slideInRight 0.3s ease;
    `;
    
    // Colores según tipo
    switch (type) {
        case 'success':
            notification.style.background = 'var(--oracle-green)';
            break;
        case 'warning':
            notification.style.background = 'var(--oracle-gold)';
            break;
        case 'error':
            notification.style.background = 'var(--oracle-red)';
            break;
        default:
            notification.style.background = 'var(--accent-primary)';
    }
    
    notification.textContent = message;
    document.body.appendChild(notification);
    
    // Auto-remover después de 5 segundos
    setTimeout(() => {
        notification.style.animation = 'slideOutRight 0.3s ease';
        setTimeout(() => {
            if (notification.parentNode) {
                notification.parentNode.removeChild(notification);
            }
        }, 300);
    }, 5000);
}

// Funciones de acciones de resultados
function downloadCalendar() {
    if (!appState.calculatedProfile) {
        showNotification('No hay perfil calculado para descargar', 'warning');
        return;
    }
    
    // Generar archivo ICS
    const icsContent = generateICSFile(appState.calculatedProfile.events);
    const blob = new Blob([icsContent], { type: 'text/calendar' });
    const url = URL.createObjectURL(blob);
    
    const a = document.createElement('a');
    a.href = url;
    a.download = 'agenda_oracular_mentalia.ics';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
    
    showNotification('Calendario descargado exitosamente', 'success');
}

function generateICSFile(events) {
    let ics = 'BEGIN:VCALENDAR\n';
    ics += 'VERSION:2.0\n';
    ics += 'PRODID:-//MENTALIA//Agenda Oracular//ES\n';
    ics += 'CALSCALE:GREGORIAN\n';
    
    events.forEach(event => {
        ics += 'BEGIN:VEVENT\n';
        ics += `UID:${event.date}-${event.title.replace(/\s+/g, '-').toLowerCase()}@mentalia.com\n`;
        ics += `DTSTART;VALUE=DATE:${event.date.replace(/-/g, '')}\n`;
        ics += `SUMMARY:${event.title}\n`;
        ics += `DESCRIPTION:${event.description}\\n\\n💫 ${event.microaction}\n`;
        ics += 'END:VEVENT\n';
    });
    
    ics += 'END:VCALENDAR';
    return ics;
}

function shareProfile() {
    if (navigator.share) {
        navigator.share({
            title: 'Mi RUT Astral - ORÁCULO MENTALIA',
            text: 'Descubre tu mapa cósmico personalizado con ORÁCULO MENTALIA',
            url: window.location.href
        });
    } else {
        // Fallback: copiar al portapapeles
        const shareText = `Descubre tu RUT Astral con ORÁCULO MENTALIA: ${window.location.href}`;
        navigator.clipboard.writeText(shareText).then(() => {
            showNotification('Enlace copiado al portapapeles', 'success');
        });
    }
}

function consultOracle() {
    showNotification('Función de consulta oracular en desarrollo. ¡Próximamente disponible!', 'info');
}

// Agregar estilos de animación
const style = document.createElement('style');
style.textContent = `
    @keyframes slideInRight {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOutRight {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Exportar funciones para uso global
window.startOnboarding = startOnboarding;
window.nextStep = nextStep;
window.previousStep = previousStep;
window.submitForm = submitForm;
window.estimateTime = estimateTime;
window.downloadCalendar = downloadCalendar;
window.shareProfile = shareProfile;
window.consultOracle = consultOracle;

