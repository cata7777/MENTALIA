# ARQUITECTURA TÉCNICA SIGN-LINK
## Especificaciones Completas para Despliegue RunPod

---

## 🏗️ ARQUITECTURA GENERAL

### Stack Tecnológico Principal:
```
Frontend Web:
├── React 18+ (TypeScript)
├── Three.js (Avatares 3D)
├── WebRTC (Streaming tiempo real)
├── Socket.io (Comunicación bidireccional)
└── Tailwind CSS (Diseño responsivo)

Backend API:
├── Python 3.11 (FastAPI)
├── Node.js 20+ (Servicios auxiliares)
├── PyTorch (Modelos IA)
├── MediaPipe (Procesamiento visual)
└── Whisper (Transcripción audio)

Base de Datos:
├── PostgreSQL 15 (Datos principales)
├── Redis 7 (Cache y sesiones)
├── MinIO (Almacenamiento archivos)
└── Elasticsearch (Búsqueda avanzada)

Infraestructura:
├── Docker & Docker Compose
├── Nginx (Proxy reverso)
├── Certbot (SSL automático)
└── Prometheus + Grafana (Monitoreo)
```

---

## 🖥️ ESPECIFICACIONES RUNPOD

### Configuración de Servidor Recomendada:
```yaml
GPU: NVIDIA A100 (80GB VRAM)
CPU: 32 vCPUs (AMD EPYC/Intel Xeon)
RAM: 128GB DDR4
Storage: 2TB NVMe SSD
Network: 1Gbps dedicado
OS: Ubuntu 22.04 LTS
```

### Distribución de Recursos:
```
GPU Allocation:
├── Reconocimiento Señas: 40GB VRAM
├── Generación Avatares: 20GB VRAM
├── Análisis Emocional: 10GB VRAM
└── Buffer/Cache: 10GB VRAM

CPU Allocation:
├── API Principal: 8 cores
├── Procesamiento Video: 12 cores
├── Base de Datos: 4 cores
├── Servicios Auxiliares: 4 cores
└── Sistema: 4 cores

RAM Allocation:
├── Modelos IA: 64GB
├── Base de Datos: 32GB
├── Cache Redis: 16GB
├── Aplicaciones: 12GB
└── Sistema: 4GB
```

---

## 🤖 MODELOS DE IA IMPLEMENTADOS

### 1. Reconocimiento de Lengua de Señas
```python
# Modelo principal: MediaPipe + YOLO v11
class SignLanguageDetector:
    def __init__(self):
        self.mediapipe_hands = mp.solutions.hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5
        )
        self.yolo_model = YOLO('yolov11n.pt')
        self.sign_classifier = self.load_sign_model()
    
    def detect_signs(self, frame):
        # Detección de manos con MediaPipe
        hand_landmarks = self.mediapipe_hands.process(frame)
        
        # Clasificación de señas
        if hand_landmarks.multi_hand_landmarks:
            signs = self.sign_classifier.predict(hand_landmarks)
            return signs
        
        return None

# Precisión esperada: >98% para vocabulario estándar
```

### 2. Generación de Avatares 3D
```python
# Integración con Ready Player Me + Three.js
class AvatarGenerator:
    def __init__(self):
        self.avatar_engine = ThreeJSEngine()
        self.animation_controller = SignAnimationController()
    
    def create_avatar(self, user_preferences):
        # Generación de avatar personalizado
        avatar = self.avatar_engine.create_from_template(
            gender=user_preferences.gender,
            style=user_preferences.style,
            clothing=user_preferences.clothing
        )
        
        # Configuración de animaciones de señas
        avatar.add_sign_animations(self.animation_controller.get_all())
        
        return avatar
    
    def animate_sign(self, avatar, sign_text):
        # Conversión texto -> secuencia de señas
        sign_sequence = self.text_to_signs(sign_text)
        
        # Animación fluida del avatar
        return avatar.animate_sequence(sign_sequence)
```

### 3. Análisis Emocional Multimodal
```python
# Integración con Motor de Análisis Comunicacional MENTALIA
class EmotionalAnalyzer:
    def __init__(self):
        self.face_analyzer = FaceEmotionDetector()
        self.voice_analyzer = VoiceEmotionDetector()
        self.text_analyzer = TextEmotionAnalyzer()
    
    def analyze_multimodal(self, video_frame, audio_chunk, text):
        # Análisis facial
        face_emotions = self.face_analyzer.detect(video_frame)
        
        # Análisis vocal
        voice_emotions = self.voice_analyzer.analyze(audio_chunk)
        
        # Análisis textual
        text_emotions = self.text_analyzer.process(text)
        
        # Fusión multimodal
        combined_analysis = self.fuse_modalities(
            face_emotions, voice_emotions, text_emotions
        )
        
        return combined_analysis
```

---

## 🌐 ARQUITECTURA WEB

### Frontend (React + Three.js):
```typescript
// Componente principal de traducción
interface SignTranslatorProps {
  mode: 'voice-to-sign' | 'sign-to-voice' | 'bidirectional';
  avatar: AvatarConfig;
  language: 'es' | 'en' | 'pt';
}

const SignTranslator: React.FC<SignTranslatorProps> = ({ 
  mode, avatar, language 
}) => {
  const [isRecording, setIsRecording] = useState(false);
  const [translation, setTranslation] = useState('');
  const canvasRef = useRef<HTMLCanvasElement>(null);
  
  // Inicialización de Three.js para avatar 3D
  useEffect(() => {
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, 16/9, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ 
      canvas: canvasRef.current 
    });
    
    // Cargar avatar 3D
    const avatarLoader = new AvatarLoader();
    avatarLoader.load(avatar.modelUrl).then(avatarModel => {
      scene.add(avatarModel);
    });
    
    return () => {
      renderer.dispose();
    };
  }, [avatar]);
  
  // Manejo de traducción en tiempo real
  const handleTranslation = useCallback(async (inputData) => {
    const response = await fetch('/api/translate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        mode,
        data: inputData,
        language,
        avatarId: avatar.id
      })
    });
    
    const result = await response.json();
    setTranslation(result.translation);
    
    // Animar avatar con la traducción
    if (mode === 'voice-to-sign') {
      animateAvatarSigns(result.signSequence);
    }
  }, [mode, language, avatar]);
  
  return (
    <div className="sign-translator">
      <canvas ref={canvasRef} className="avatar-canvas" />
      <div className="translation-output">{translation}</div>
      <button 
        onClick={() => setIsRecording(!isRecording)}
        className="record-button"
      >
        {isRecording ? 'Detener' : 'Iniciar'} Traducción
      </button>
    </div>
  );
};
```

### Backend API (FastAPI):
```python
from fastapi import FastAPI, WebSocket, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import cv2
import numpy as np

app = FastAPI(title="Sign-Link API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicialización de modelos IA
sign_detector = SignLanguageDetector()
avatar_generator = AvatarGenerator()
emotion_analyzer = EmotionalAnalyzer()

@app.post("/api/translate")
async def translate_content(request: TranslationRequest):
    """Endpoint principal de traducción"""
    
    if request.mode == "voice-to-sign":
        # Transcribir audio a texto
        text = await transcribe_audio(request.audio_data)
        
        # Generar secuencia de señas
        sign_sequence = await text_to_signs(text)
        
        # Crear animación para avatar
        animation = await generate_avatar_animation(
            sign_sequence, request.avatar_id
        )
        
        return {
            "translation": text,
            "sign_sequence": sign_sequence,
            "animation": animation
        }
    
    elif request.mode == "sign-to-voice":
        # Detectar señas en video
        signs = await detect_signs_from_video(request.video_data)
        
        # Convertir señas a texto
        text = await signs_to_text(signs)
        
        # Generar audio con voz sintética
        audio = await text_to_speech(text, request.voice_config)
        
        return {
            "translation": text,
            "detected_signs": signs,
            "audio_url": audio.url
        }

@app.websocket("/ws/realtime-translation")
async def websocket_translation(websocket: WebSocket):
    """WebSocket para traducción en tiempo real"""
    await websocket.accept()
    
    try:
        while True:
            # Recibir frame de video
            data = await websocket.receive_bytes()
            frame = cv2.imdecode(np.frombuffer(data, np.uint8), cv2.IMREAD_COLOR)
            
            # Procesar frame
            signs = sign_detector.detect_signs(frame)
            emotions = emotion_analyzer.analyze_frame(frame)
            
            # Enviar resultados
            await websocket.send_json({
                "signs": signs,
                "emotions": emotions,
                "timestamp": time.time()
            })
            
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        await websocket.close()

@app.get("/api/avatars")
async def list_avatars():
    """Listar avatares disponibles"""
    return await avatar_generator.get_available_avatars()

@app.post("/api/avatars/create")
async def create_custom_avatar(config: AvatarConfig):
    """Crear avatar personalizado"""
    avatar = await avatar_generator.create_avatar(config)
    return {"avatar_id": avatar.id, "model_url": avatar.model_url}
```

---

## 📱 APLICACIÓN MÓVIL

### React Native + TensorFlow Lite:
```typescript
// Componente principal móvil
import { Camera } from 'expo-camera';
import * as tf from '@tensorflow/tfjs';
import '@tensorflow/tfjs-react-native';

interface MobileTranslatorProps {
  mode: TranslationMode;
}

const MobileTranslator: React.FC<MobileTranslatorProps> = ({ mode }) => {
  const [hasPermission, setHasPermission] = useState<boolean | null>(null);
  const [model, setModel] = useState<tf.LayersModel | null>(null);
  const cameraRef = useRef<Camera>(null);
  
  // Cargar modelo TensorFlow Lite
  useEffect(() => {
    const loadModel = async () => {
      try {
        const modelUrl = 'https://mentalia.com/models/sign-detection-mobile.json';
        const loadedModel = await tf.loadLayersModel(modelUrl);
        setModel(loadedModel);
      } catch (error) {
        console.error('Error loading model:', error);
      }
    };
    
    loadModel();
  }, []);
  
  // Procesar frame de cámara
  const processFrame = useCallback(async (imageUri: string) => {
    if (!model) return;
    
    // Convertir imagen a tensor
    const response = await fetch(imageUri, {}, { isBinary: true });
    const imageData = await response.arrayBuffer();
    const imageTensor = tf.node.decodeImage(new Uint8Array(imageData));
    
    // Realizar predicción
    const prediction = model.predict(imageTensor) as tf.Tensor;
    const results = await prediction.data();
    
    // Procesar resultados
    const detectedSigns = processModelOutput(results);
    
    return detectedSigns;
  }, [model]);
  
  // Configuración de cámara
  const takePicture = async () => {
    if (cameraRef.current) {
      const photo = await cameraRef.current.takePictureAsync();
      const signs = await processFrame(photo.uri);
      
      // Enviar a servidor para procesamiento completo si es necesario
      if (signs.confidence < 0.8) {
        const serverResult = await sendToServer(photo.uri);
        return serverResult;
      }
      
      return signs;
    }
  };
  
  return (
    <View style={styles.container}>
      <Camera
        ref={cameraRef}
        style={styles.camera}
        type={Camera.Constants.Type.front}
        onCameraReady={() => console.log('Camera ready')}
      />
      
      <View style={styles.controls}>
        <TouchableOpacity 
          style={styles.captureButton}
          onPress={takePicture}
        >
          <Text style={styles.buttonText}>Traducir</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
};
```

---

## 🗄️ BASE DE DATOS

### Esquema PostgreSQL:
```sql
-- Usuarios y perfiles
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Avatares personalizados
CREATE TABLE avatars (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    name VARCHAR(100) NOT NULL,
    model_url TEXT NOT NULL,
    configuration JSONB NOT NULL,
    is_public BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Sesiones de traducción
CREATE TABLE translation_sessions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    avatar_id UUID REFERENCES avatars(id),
    mode VARCHAR(50) NOT NULL, -- 'voice-to-sign', 'sign-to-voice'
    duration_seconds INTEGER,
    accuracy_score FLOAT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Intérpretes profesionales (marketplace)
CREATE TABLE interpreters (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    specializations TEXT[] NOT NULL,
    hourly_rate DECIMAL(10,2),
    rating DECIMAL(3,2) DEFAULT 0.00,
    total_sessions INTEGER DEFAULT 0,
    is_verified BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Reservas de intérpretes
CREATE TABLE interpreter_bookings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    client_id UUID REFERENCES users(id),
    interpreter_id UUID REFERENCES interpreters(id),
    scheduled_at TIMESTAMP NOT NULL,
    duration_minutes INTEGER NOT NULL,
    status VARCHAR(50) DEFAULT 'pending',
    total_cost DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT NOW()
);

-- Empresas (API B2B)
CREATE TABLE enterprise_clients (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    company_name VARCHAR(255) NOT NULL,
    contact_email VARCHAR(255) NOT NULL,
    api_key VARCHAR(255) UNIQUE NOT NULL,
    monthly_quota INTEGER DEFAULT 10000,
    usage_count INTEGER DEFAULT 0,
    plan_type VARCHAR(50) DEFAULT 'basic',
    created_at TIMESTAMP DEFAULT NOW()
);

-- Métricas de uso
CREATE TABLE usage_metrics (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    session_id UUID REFERENCES translation_sessions(id),
    metric_type VARCHAR(100) NOT NULL,
    metric_value JSONB NOT NULL,
    recorded_at TIMESTAMP DEFAULT NOW()
);

-- Índices para optimización
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_avatars_user_id ON avatars(user_id);
CREATE INDEX idx_sessions_user_id ON translation_sessions(user_id);
CREATE INDEX idx_interpreters_rating ON interpreters(rating DESC);
CREATE INDEX idx_bookings_scheduled ON interpreter_bookings(scheduled_at);
CREATE INDEX idx_metrics_recorded ON usage_metrics(recorded_at);
```

### Configuración Redis:
```redis
# Cache de sesiones de usuario
SET user:session:{user_id} "{session_data}" EX 3600

# Cache de modelos IA frecuentes
SET model:signs:cache "{model_predictions}" EX 1800

# Rate limiting para API
SET api:limit:{api_key} 1000 EX 3600

# Cache de avatares populares
SET avatar:popular "{avatar_list}" EX 7200

# WebSocket connections tracking
SADD websocket:active {connection_id}
```

---

## 🔧 CONFIGURACIÓN DE DESPLIEGUE

### Docker Compose:
```yaml
version: '3.8'

services:
  # API Principal
  sign-link-api:
    build: 
      context: ./backend
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:pass@postgres:5432/signlink
      - REDIS_URL=redis://redis:6379
      - GPU_ENABLED=true
    volumes:
      - ./models:/app/models
      - ./uploads:/app/uploads
    depends_on:
      - postgres
      - redis
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]

  # Frontend Web
  sign-link-web:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    ports:
      - "3000:3000"
    environment:
      - REACT_APP_API_URL=http://sign-link-api:8000
      - REACT_APP_WS_URL=ws://sign-link-api:8000/ws
    depends_on:
      - sign-link-api

  # Base de datos
  postgres:
    image: postgres:15
    environment:
      - POSTGRES_DB=signlink
      - POSTGRES_USER=signlink_user
      - POSTGRES_PASSWORD=secure_password
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql
    ports:
      - "5432:5432"

  # Cache Redis
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data

  # Proxy Nginx
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - ./ssl:/etc/nginx/ssl
    depends_on:
      - sign-link-web
      - sign-link-api

  # Monitoreo
  prometheus:
    image: prom/prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml

  grafana:
    image: grafana/grafana
    ports:
      - "3001:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
    volumes:
      - grafana_data:/var/lib/grafana

volumes:
  postgres_data:
  redis_data:
  grafana_data:
```

### Nginx Configuration:
```nginx
upstream sign_link_api {
    server sign-link-api:8000;
}

upstream sign_link_web {
    server sign-link-web:3000;
}

server {
    listen 80;
    server_name mentalia.com;
    
    # Redirigir HTTP a HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name mentalia.com;
    
    ssl_certificate /etc/nginx/ssl/cert.pem;
    ssl_certificate_key /etc/nginx/ssl/key.pem;
    
    # Configuración SSL moderna
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512;
    ssl_prefer_server_ciphers off;
    
    # Sign-Link routes
    location /SignLink/ {
        proxy_pass http://sign_link_web/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    
    location /SignLink/api/ {
        proxy_pass http://sign_link_api/api/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    
    # WebSocket support
    location /SignLink/ws/ {
        proxy_pass http://sign_link_api/ws/;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    
    # Archivos estáticos con cache
    location /SignLink/static/ {
        proxy_pass http://sign_link_web/static/;
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
}
```

---

## 📊 MONITOREO Y MÉTRICAS

### Prometheus Metrics:
```python
from prometheus_client import Counter, Histogram, Gauge
import time

# Métricas de traducción
translation_requests = Counter(
    'sign_link_translation_requests_total',
    'Total translation requests',
    ['mode', 'language']
)

translation_duration = Histogram(
    'sign_link_translation_duration_seconds',
    'Translation processing time',
    ['mode']
)

active_users = Gauge(
    'sign_link_active_users',
    'Currently active users'
)

# Métricas de precisión
model_accuracy = Gauge(
    'sign_link_model_accuracy',
    'Current model accuracy',
    ['model_type']
)

# Middleware para métricas
@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start_time = time.time()
    
    response = await call_next(request)
    
    # Registrar duración
    duration = time.time() - start_time
    translation_duration.observe(duration)
    
    # Contar requests
    if "/api/translate" in str(request.url):
        translation_requests.inc()
    
    return response
```

### Grafana Dashboard:
```json
{
  "dashboard": {
    "title": "Sign-Link Metrics",
    "panels": [
      {
        "title": "Translation Requests/min",
        "type": "graph",
        "targets": [
          {
            "expr": "rate(sign_link_translation_requests_total[1m])",
            "legendFormat": "{{mode}} - {{language}}"
          }
        ]
      },
      {
        "title": "Average Response Time",
        "type": "singlestat",
        "targets": [
          {
            "expr": "avg(sign_link_translation_duration_seconds)",
            "legendFormat": "Avg Response Time"
          }
        ]
      },
      {
        "title": "Model Accuracy",
        "type": "gauge",
        "targets": [
          {
            "expr": "sign_link_model_accuracy",
            "legendFormat": "{{model_type}}"
          }
        ]
      },
      {
        "title": "Active Users",
        "type": "singlestat",
        "targets": [
          {
            "expr": "sign_link_active_users",
            "legendFormat": "Active Users"
          }
        ]
      }
    ]
  }
}
```

---

## 🔒 SEGURIDAD

### Autenticación JWT:
```python
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

SECRET_KEY = "your-secret-key-here"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise JWTError("Invalid token")
        return user_id
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
```

### Rate Limiting:
```python
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.post("/api/translate")
@limiter.limit("10/minute")  # 10 requests per minute
async def translate_endpoint(request: Request, data: TranslationRequest):
    # Translation logic here
    pass
```

---

## 🚀 COMANDOS DE DESPLIEGUE

### Script de Instalación Automática:
```bash
#!/bin/bash
# install_sign_link.sh

echo "🚀 Iniciando instalación de Sign-Link..."

# Verificar prerrequisitos
if ! command -v docker &> /dev/null; then
    echo "❌ Docker no está instalado"
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose no está instalado"
    exit 1
fi

# Crear directorios necesarios
mkdir -p {models,uploads,ssl,logs}

# Descargar modelos IA
echo "📥 Descargando modelos de IA..."
wget -O models/sign-detection.pt "https://mentalia.com/models/sign-detection.pt"
wget -O models/emotion-analysis.pt "https://mentalia.com/models/emotion-analysis.pt"

# Configurar variables de entorno
if [ ! -f .env ]; then
    echo "⚙️ Configurando variables de entorno..."
    cp .env.example .env
    
    # Generar claves seguras
    export SECRET_KEY=$(openssl rand -hex 32)
    export DB_PASSWORD=$(openssl rand -hex 16)
    
    # Actualizar .env
    sed -i "s/SECRET_KEY=.*/SECRET_KEY=$SECRET_KEY/" .env
    sed -i "s/DB_PASSWORD=.*/DB_PASSWORD=$DB_PASSWORD/" .env
fi

# Generar certificados SSL
if [ ! -f ssl/cert.pem ]; then
    echo "🔒 Generando certificados SSL..."
    openssl req -x509 -newkey rsa:4096 -keyout ssl/key.pem -out ssl/cert.pem -days 365 -nodes \
        -subj "/C=US/ST=State/L=City/O=Organization/CN=mentalia.com"
fi

# Construir y desplegar
echo "🏗️ Construyendo contenedores..."
docker-compose build

echo "🚀 Desplegando aplicación..."
docker-compose up -d

# Verificar despliegue
echo "🔍 Verificando despliegue..."
sleep 30

if curl -f http://localhost:8000/health; then
    echo "✅ Sign-Link desplegado exitosamente!"
    echo "🌐 Accede a: https://mentalia.com/SignLink"
    echo "📚 API Docs: https://mentalia.com/SignLink/docs"
else
    echo "❌ Error en el despliegue. Revisa los logs:"
    docker-compose logs
fi
```

### Comandos de Mantenimiento:
```bash
# Backup de base de datos
docker-compose exec postgres pg_dump -U signlink_user signlink > backup_$(date +%Y%m%d).sql

# Restaurar backup
docker-compose exec -T postgres psql -U signlink_user signlink < backup_20240130.sql

# Ver logs en tiempo real
docker-compose logs -f sign-link-api

# Actualizar modelos IA
docker-compose exec sign-link-api python update_models.py

# Reiniciar servicios
docker-compose restart sign-link-api

# Limpiar cache
docker-compose exec redis redis-cli FLUSHALL
```

---

**Esta arquitectura técnica proporciona una base sólida, escalable y segura para Sign-Link, optimizada específicamente para despliegue en RunPod con integración completa al ecosistema MENTALIA.**

