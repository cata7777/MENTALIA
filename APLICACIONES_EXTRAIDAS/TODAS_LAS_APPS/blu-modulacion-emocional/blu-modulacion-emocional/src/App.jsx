import { useState, useEffect } from 'react'
import { Button } from '@/components/ui/button.jsx'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card.jsx'
import { Badge } from '@/components/ui/badge.jsx'
import { Progress } from '@/components/ui/progress.jsx'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs.jsx'
import { 
  Heart, 
  Brain, 
  Sparkles, 
  Target, 
  Activity, 
  Smile,
  Frown,
  Zap,
  Sun,
  Cloud,
  Star,
  Flame,
  Droplets,
  Wind,
  Mountain,
  Leaf,
  User,
  Settings,
  BookOpen,
  Play,
  Pause,
  RotateCcw,
  ChevronRight,
  Filter,
  Search,
  Calendar,
  Clock,
  TrendingUp,
  Award,
  Users
} from 'lucide-react'
import './App.css'

function App() {
  const [perfilActivo, setPerfilActivo] = useState('CEA')
  const [emocionSeleccionada, setEmocionSeleccionada] = useState(null)
  const [filtroNucleo, setFiltroNucleo] = useState('Todos')
  const [busqueda, setBusqueda] = useState('')

  // Base de datos de las 64 emociones ND
  const emociones64 = [
    // Núcleo: Alegría
    { id: 1, nucleo: 'Alegría', emocion: 'Gozo', color: 'bg-yellow-400', intensidad: 'alta', frecuencia: 'media' },
    { id: 2, nucleo: 'Alegría', emocion: 'Gratitud', color: 'bg-yellow-300', intensidad: 'media', frecuencia: 'alta' },
    { id: 3, nucleo: 'Alegría', emocion: 'Entusiasmo', color: 'bg-orange-400', intensidad: 'alta', frecuencia: 'media' },
    { id: 4, nucleo: 'Alegría', emocion: 'Euforia', color: 'bg-pink-400', intensidad: 'muy_alta', frecuencia: 'baja' },
    { id: 5, nucleo: 'Alegría', emocion: 'Satisfacción', color: 'bg-green-300', intensidad: 'media', frecuencia: 'alta' },
    { id: 6, nucleo: 'Alegría', emocion: 'Diversión', color: 'bg-purple-300', intensidad: 'media', frecuencia: 'media' },
    { id: 7, nucleo: 'Alegría', emocion: 'Esperanza', color: 'bg-blue-300', intensidad: 'media', frecuencia: 'alta' },
    { id: 8, nucleo: 'Alegría', emocion: 'Optimismo', color: 'bg-cyan-300', intensidad: 'media', frecuencia: 'media' },

    // Núcleo: Tristeza
    { id: 9, nucleo: 'Tristeza', emocion: 'Melancolía', color: 'bg-blue-500', intensidad: 'media', frecuencia: 'media' },
    { id: 10, nucleo: 'Tristeza', emocion: 'Nostalgia', color: 'bg-indigo-400', intensidad: 'media', frecuencia: 'media' },
    { id: 11, nucleo: 'Tristeza', emocion: 'Pena', color: 'bg-gray-500', intensidad: 'alta', frecuencia: 'baja' },
    { id: 12, nucleo: 'Tristeza', emocion: 'Desaliento', color: 'bg-slate-500', intensidad: 'media', frecuencia: 'media' },
    { id: 13, nucleo: 'Tristeza', emocion: 'Soledad', color: 'bg-blue-600', intensidad: 'alta', frecuencia: 'media' },
    { id: 14, nucleo: 'Tristeza', emocion: 'Vacío', color: 'bg-gray-600', intensidad: 'alta', frecuencia: 'baja' },
    { id: 15, nucleo: 'Tristeza', emocion: 'Duelo', color: 'bg-black', intensidad: 'muy_alta', frecuencia: 'baja' },
    { id: 16, nucleo: 'Tristeza', emocion: 'Añoranza', color: 'bg-violet-500', intensidad: 'media', frecuencia: 'media' },

    // Núcleo: Ira
    { id: 17, nucleo: 'Ira', emocion: 'Frustración', color: 'bg-red-500', intensidad: 'alta', frecuencia: 'alta' },
    { id: 18, nucleo: 'Ira', emocion: 'Irritación', color: 'bg-orange-500', intensidad: 'media', frecuencia: 'alta' },
    { id: 19, nucleo: 'Ira', emocion: 'Indignación', color: 'bg-red-600', intensidad: 'alta', frecuencia: 'media' },
    { id: 20, nucleo: 'Ira', emocion: 'Rabia', color: 'bg-red-700', intensidad: 'muy_alta', frecuencia: 'baja' },
    { id: 21, nucleo: 'Ira', emocion: 'Molestia', color: 'bg-yellow-600', intensidad: 'baja', frecuencia: 'alta' },
    { id: 22, nucleo: 'Ira', emocion: 'Enojo', color: 'bg-red-400', intensidad: 'media', frecuencia: 'media' },
    { id: 23, nucleo: 'Ira', emocion: 'Cólera', color: 'bg-red-800', intensidad: 'muy_alta', frecuencia: 'muy_baja' },
    { id: 24, nucleo: 'Ira', emocion: 'Impaciencia', color: 'bg-amber-500', intensidad: 'media', frecuencia: 'muy_alta' },

    // Núcleo: Miedo
    { id: 25, nucleo: 'Miedo', emocion: 'Ansiedad', color: 'bg-purple-600', intensidad: 'alta', frecuencia: 'muy_alta' },
    { id: 26, nucleo: 'Miedo', emocion: 'Nerviosismo', color: 'bg-purple-400', intensidad: 'media', frecuencia: 'alta' },
    { id: 27, nucleo: 'Miedo', emocion: 'Preocupación', color: 'bg-indigo-500', intensidad: 'media', frecuencia: 'muy_alta' },
    { id: 28, nucleo: 'Miedo', emocion: 'Pánico', color: 'bg-purple-800', intensidad: 'muy_alta', frecuencia: 'baja' },
    { id: 29, nucleo: 'Miedo', emocion: 'Inseguridad', color: 'bg-gray-400', intensidad: 'media', frecuencia: 'alta' },
    { id: 30, nucleo: 'Miedo', emocion: 'Timidez', color: 'bg-pink-300', intensidad: 'baja', frecuencia: 'media' },
    { id: 31, nucleo: 'Miedo', emocion: 'Terror', color: 'bg-black', intensidad: 'muy_alta', frecuencia: 'muy_baja' },
    { id: 32, nucleo: 'Miedo', emocion: 'Inquietud', color: 'bg-slate-400', intensidad: 'media', frecuencia: 'alta' },

    // Núcleo: Sorpresa
    { id: 33, nucleo: 'Sorpresa', emocion: 'Asombro', color: 'bg-cyan-400', intensidad: 'alta', frecuencia: 'media' },
    { id: 34, nucleo: 'Sorpresa', emocion: 'Admiración', color: 'bg-teal-400', intensidad: 'media', frecuencia: 'media' },
    { id: 35, nucleo: 'Sorpresa', emocion: 'Curiosidad', color: 'bg-emerald-400', intensidad: 'media', frecuencia: 'muy_alta' },
    { id: 36, nucleo: 'Sorpresa', emocion: 'Fascinación', color: 'bg-violet-400', intensidad: 'alta', frecuencia: 'media' },
    { id: 37, nucleo: 'Sorpresa', emocion: 'Perplejidad', color: 'bg-gray-300', intensidad: 'media', frecuencia: 'media' },
    { id: 38, nucleo: 'Sorpresa', emocion: 'Desconcierto', color: 'bg-slate-300', intensidad: 'media', frecuencia: 'media' },
    { id: 39, nucleo: 'Sorpresa', emocion: 'Estupor', color: 'bg-zinc-400', intensidad: 'alta', frecuencia: 'baja' },
    { id: 40, nucleo: 'Sorpresa', emocion: 'Maravilla', color: 'bg-sky-400', intensidad: 'alta', frecuencia: 'baja' },

    // Núcleo: Confianza
    { id: 41, nucleo: 'Confianza', emocion: 'Seguridad', color: 'bg-green-500', intensidad: 'media', frecuencia: 'media' },
    { id: 42, nucleo: 'Confianza', emocion: 'Tranquilidad', color: 'bg-blue-200', intensidad: 'baja', frecuencia: 'alta' },
    { id: 43, nucleo: 'Confianza', emocion: 'Serenidad', color: 'bg-teal-200', intensidad: 'baja', frecuencia: 'media' },
    { id: 44, nucleo: 'Confianza', emocion: 'Calma', color: 'bg-green-200', intensidad: 'baja', frecuencia: 'media' },
    { id: 45, nucleo: 'Confianza', emocion: 'Paz', color: 'bg-emerald-200', intensidad: 'baja', frecuencia: 'baja' },
    { id: 46, nucleo: 'Confianza', emocion: 'Estabilidad', color: 'bg-stone-300', intensidad: 'media', frecuencia: 'media' },
    { id: 47, nucleo: 'Confianza', emocion: 'Firmeza', color: 'bg-slate-600', intensidad: 'media', frecuencia: 'media' },
    { id: 48, nucleo: 'Confianza', emocion: 'Determinación', color: 'bg-gray-700', intensidad: 'alta', frecuencia: 'media' },

    // Núcleo: Anticipación
    { id: 49, nucleo: 'Anticipación', emocion: 'Expectativa', color: 'bg-amber-400', intensidad: 'media', frecuencia: 'alta' },
    { id: 50, nucleo: 'Anticipación', emocion: 'Ilusión', color: 'bg-pink-400', intensidad: 'alta', frecuencia: 'media' },
    { id: 51, nucleo: 'Anticipación', emocion: 'Emoción', color: 'bg-rose-400', intensidad: 'alta', frecuencia: 'media' },
    { id: 52, nucleo: 'Anticipación', emocion: 'Anhelo', color: 'bg-purple-300', intensidad: 'media', frecuencia: 'media' },
    { id: 53, nucleo: 'Anticipación', emocion: 'Deseo', color: 'bg-red-300', intensidad: 'media', frecuencia: 'alta' },
    { id: 54, nucleo: 'Anticipación', emocion: 'Ansia', color: 'bg-orange-600', intensidad: 'alta', frecuencia: 'media' },
    { id: 55, nucleo: 'Anticipación', emocion: 'Impaciencia', color: 'bg-yellow-500', intensidad: 'media', frecuencia: 'muy_alta' },
    { id: 56, nucleo: 'Anticipación', emocion: 'Urgencia', color: 'bg-red-500', intensidad: 'alta', frecuencia: 'alta' },

    // Núcleo: Disgusto
    { id: 57, nucleo: 'Disgusto', emocion: 'Repulsión', color: 'bg-green-700', intensidad: 'alta', frecuencia: 'baja' },
    { id: 58, nucleo: 'Disgusto', emocion: 'Aversión', color: 'bg-lime-700', intensidad: 'media', frecuencia: 'media' },
    { id: 59, nucleo: 'Disgusto', emocion: 'Rechazo', color: 'bg-emerald-700', intensidad: 'media', frecuencia: 'media' },
    { id: 60, nucleo: 'Disgusto', emocion: 'Desprecio', color: 'bg-teal-700', intensidad: 'alta', frecuencia: 'baja' },
    { id: 61, nucleo: 'Disgusto', emocion: 'Desdén', color: 'bg-cyan-700', intensidad: 'media', frecuencia: 'baja' },
    { id: 62, nucleo: 'Disgusto', emocion: 'Asco', color: 'bg-green-800', intensidad: 'alta', frecuencia: 'baja' },
    { id: 63, nucleo: 'Disgusto', emocion: 'Náusea', color: 'bg-lime-800', intensidad: 'alta', frecuencia: 'baja' },
    { id: 64, nucleo: 'Disgusto', emocion: 'Hastío', color: 'bg-stone-600', intensidad: 'media', frecuencia: 'media' }
  ]

  const nucleos = ['Todos', 'Alegría', 'Tristeza', 'Ira', 'Miedo', 'Sorpresa', 'Confianza', 'Anticipación', 'Disgusto']
  const perfiles = ['CEA', 'TDAH', 'Altas_Capacidades']

  const [emocionesFiltradas, setEmocionesFiltradas] = useState(emociones64)

  useEffect(() => {
    let filtradas = emociones64
    
    if (filtroNucleo !== 'Todos') {
      filtradas = filtradas.filter(emocion => emocion.nucleo === filtroNucleo)
    }
    
    if (busqueda) {
      filtradas = filtradas.filter(emocion => 
        emocion.emocion.toLowerCase().includes(busqueda.toLowerCase()) ||
        emocion.nucleo.toLowerCase().includes(busqueda.toLowerCase())
      )
    }
    
    setEmocionesFiltradas(filtradas)
  }, [filtroNucleo, busqueda])

  const getEmocionData = (emocion) => {
    const estrategias = {
      CEA: `Actividad específica para CEA relacionada con ${emocion.emocion}`,
      TDAH: `Actividad específica para TDAH relacionada con ${emocion.emocion}`,
      Altas_Capacidades: `Actividad específica para Altas Capacidades relacionada con ${emocion.emocion}`
    }

    const definicion = `${emocion.emocion} es una emoción del núcleo ${emocion.nucleo} que se manifiesta de manera única en personas neurodivergentes.`
    
    const matizND = {
      CEA: `Para personas CEA, ${emocion.emocion} puede manifestarse de manera más intensa o diferente debido a la sensibilidad sensorial.`,
      TDAH: `Para personas con TDAH, ${emocion.emocion} puede ser más intensa y requerir estrategias específicas de regulación.`,
      Altas_Capacidades: `Para personas con Altas Capacidades, ${emocion.emocion} puede ser más compleja y profunda.`
    }

    return { estrategias, definicion, matizND }
  }

  const stats = {
    totalEmociones: 64,
    nucleosActivos: 8,
    perfilesND: 3,
    sesionesHoy: 23
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-pink-50 via-purple-50 to-blue-50">
      {/* Header */}
      <header className="bg-white/80 backdrop-blur-sm border-b border-pink-200 sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            <div className="flex items-center space-x-3">
              <div className="w-10 h-10 bg-gradient-to-r from-pink-500 to-purple-500 rounded-xl flex items-center justify-center">
                <Heart className="w-6 h-6 text-white" />
              </div>
              <div>
                <h1 className="text-xl font-bold bg-gradient-to-r from-pink-600 to-purple-600 bg-clip-text text-transparent">
                  BLU Modulación Emocional
                </h1>
                <p className="text-sm text-gray-600">64 Emociones Neurodivergentes</p>
              </div>
            </div>
            
            <div className="flex items-center space-x-4">
              <Badge variant="secondary" className="bg-pink-100 text-pink-700">
                <Sparkles className="w-3 h-3 mr-1" />
                {stats.totalEmociones} emociones
              </Badge>
              <Button variant="outline" size="sm">
                <User className="w-4 h-4 mr-2" />
                Perfil ND
              </Button>
            </div>
          </div>
        </div>
      </header>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Stats Dashboard */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
          <Card className="bg-gradient-to-r from-pink-500 to-pink-600 text-white">
            <CardContent className="p-6">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-pink-100">Emociones ND</p>
                  <p className="text-2xl font-bold">{stats.totalEmociones}</p>
                </div>
                <Heart className="w-8 h-8 text-pink-200" />
              </div>
            </CardContent>
          </Card>

          <Card className="bg-gradient-to-r from-purple-500 to-purple-600 text-white">
            <CardContent className="p-6">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-purple-100">Núcleos Emocionales</p>
                  <p className="text-2xl font-bold">{stats.nucleosActivos}</p>
                </div>
                <Brain className="w-8 h-8 text-purple-200" />
              </div>
            </CardContent>
          </Card>

          <Card className="bg-gradient-to-r from-blue-500 to-blue-600 text-white">
            <CardContent className="p-6">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-blue-100">Perfiles ND</p>
                  <p className="text-2xl font-bold">{stats.perfilesND}</p>
                </div>
                <Users className="w-8 h-8 text-blue-200" />
              </div>
            </CardContent>
          </Card>

          <Card className="bg-gradient-to-r from-green-500 to-green-600 text-white">
            <CardContent className="p-6">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-green-100">Sesiones Hoy</p>
                  <p className="text-2xl font-bold">{stats.sesionesHoy}</p>
                </div>
                <Activity className="w-8 h-8 text-green-200" />
              </div>
            </CardContent>
          </Card>
        </div>

        {/* Selector de Perfil ND */}
        <Card className="mb-8 bg-gradient-to-r from-purple-50 to-pink-50 border-purple-200">
          <CardHeader>
            <CardTitle className="flex items-center space-x-2">
              <Target className="w-5 h-5 text-purple-600" />
              <span>Selecciona tu Perfil Neurodivergente</span>
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="flex flex-wrap gap-3">
              {perfiles.map((perfil) => (
                <Button
                  key={perfil}
                  variant={perfilActivo === perfil ? "default" : "outline"}
                  onClick={() => setPerfilActivo(perfil)}
                  className="flex items-center space-x-2"
                >
                  <Brain className="w-4 h-4" />
                  <span>{perfil.replace('_', ' ')}</span>
                </Button>
              ))}
            </div>
          </CardContent>
        </Card>

        {/* Filtros y Búsqueda */}
        <div className="mb-6 space-y-4">
          <div className="flex flex-wrap gap-2">
            {nucleos.map((nucleo) => (
              <Button
                key={nucleo}
                variant={filtroNucleo === nucleo ? "default" : "outline"}
                onClick={() => setFiltroNucleo(nucleo)}
                size="sm"
              >
                {nucleo}
              </Button>
            ))}
          </div>
          
          <div className="relative max-w-md">
            <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-4 h-4" />
            <input
              type="text"
              placeholder="Buscar emoción..."
              value={busqueda}
              onChange={(e) => setBusqueda(e.target.value)}
              className="pl-10 pr-4 py-2 border border-gray-300 rounded-lg w-full focus:ring-2 focus:ring-purple-500 focus:border-transparent"
            />
          </div>
        </div>

        {/* Grid de Emociones */}
        <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 xl:grid-cols-8 gap-4 mb-8">
          {emocionesFiltradas.map((emocion) => (
            <Card 
              key={emocion.id}
              className="hover:shadow-lg transition-all duration-300 cursor-pointer group"
              onClick={() => setEmocionSeleccionada(emocion)}
            >
              <CardContent className="p-4 text-center">
                <div className={`w-12 h-12 ${emocion.color} rounded-full mx-auto mb-3 group-hover:scale-110 transition-transform flex items-center justify-center`}>
                  <Heart className="w-6 h-6 text-white" />
                </div>
                <h3 className="font-semibold text-sm mb-1 group-hover:text-purple-600 transition-colors">
                  {emocion.emocion}
                </h3>
                <p className="text-xs text-gray-600">{emocion.nucleo}</p>
                <Badge variant="outline" className="text-xs mt-2">
                  {emocion.intensidad}
                </Badge>
              </CardContent>
            </Card>
          ))}
        </div>

        {/* Modal de Emoción Seleccionada */}
        {emocionSeleccionada && (
          <Card className="mb-8 border-2 border-purple-300 bg-gradient-to-r from-purple-50 to-pink-50">
            <CardHeader>
              <div className="flex items-center justify-between">
                <CardTitle className="flex items-center space-x-3">
                  <div className={`w-12 h-12 ${emocionSeleccionada.color} rounded-full flex items-center justify-center`}>
                    <Heart className="w-6 h-6 text-white" />
                  </div>
                  <div>
                    <h2 className="text-2xl">{emocionSeleccionada.emocion}</h2>
                    <p className="text-gray-600">Núcleo: {emocionSeleccionada.nucleo}</p>
                  </div>
                </CardTitle>
                <Button variant="outline" onClick={() => setEmocionSeleccionada(null)}>
                  ✕
                </Button>
              </div>
            </CardHeader>
            <CardContent>
              <Tabs defaultValue="definicion" className="w-full">
                <TabsList className="grid w-full grid-cols-4">
                  <TabsTrigger value="definicion">Definición</TabsTrigger>
                  <TabsTrigger value="matiz">Matiz ND</TabsTrigger>
                  <TabsTrigger value="estrategia">Estrategia</TabsTrigger>
                  <TabsTrigger value="actividad">Actividad</TabsTrigger>
                </TabsList>
                
                <TabsContent value="definicion" className="mt-6">
                  <div className="space-y-4">
                    <h3 className="font-semibold text-lg">¿Qué es {emocionSeleccionada.emocion}?</h3>
                    <p className="text-gray-700">
                      {getEmocionData(emocionSeleccionada).definicion}
                    </p>
                    <div className="grid grid-cols-2 gap-4">
                      <div>
                        <p className="text-sm text-gray-600">Intensidad</p>
                        <Badge className="mt-1">{emocionSeleccionada.intensidad}</Badge>
                      </div>
                      <div>
                        <p className="text-sm text-gray-600">Frecuencia</p>
                        <Badge variant="outline" className="mt-1">{emocionSeleccionada.frecuencia}</Badge>
                      </div>
                    </div>
                  </div>
                </TabsContent>
                
                <TabsContent value="matiz" className="mt-6">
                  <div className="space-y-4">
                    <h3 className="font-semibold text-lg">Matiz Neurodivergente</h3>
                    <p className="text-gray-700">
                      {getEmocionData(emocionSeleccionada).matizND[perfilActivo]}
                    </p>
                  </div>
                </TabsContent>
                
                <TabsContent value="estrategia" className="mt-6">
                  <div className="space-y-4">
                    <h3 className="font-semibold text-lg">Estrategia para {perfilActivo.replace('_', ' ')}</h3>
                    <div className="bg-white p-4 rounded-lg border">
                      <p className="text-gray-700">
                        {getEmocionData(emocionSeleccionada).estrategias[perfilActivo]}
                      </p>
                    </div>
                  </div>
                </TabsContent>
                
                <TabsContent value="actividad" className="mt-6">
                  <div className="space-y-4">
                    <h3 className="font-semibold text-lg">Actividad Neuroafirmativa</h3>
                    <div className="bg-gradient-to-r from-purple-100 to-pink-100 p-6 rounded-lg">
                      <div className="flex items-center space-x-2 mb-4">
                        <Play className="w-5 h-5 text-purple-600" />
                        <span className="font-medium">Actividad para {perfilActivo.replace('_', ' ')}</span>
                      </div>
                      <p className="text-gray-700 mb-4">
                        Actividad específica diseñada para trabajar con {emocionSeleccionada.emocion} desde una perspectiva neuroafirmativa.
                      </p>
                      <Button className="w-full">
                        <BookOpen className="w-4 h-4 mr-2" />
                        Iniciar Actividad
                      </Button>
                    </div>
                  </div>
                </TabsContent>
              </Tabs>
            </CardContent>
          </Card>
        )}

        {/* Footer */}
        <footer className="mt-16 text-center py-8 border-t border-purple-200">
          <div className="flex items-center justify-center space-x-2 mb-4">
            <Heart className="w-6 h-6 text-purple-600" />
            <span className="text-lg font-semibold bg-gradient-to-r from-purple-600 to-pink-600 bg-clip-text text-transparent">
              BLU Modulación Emocional
            </span>
          </div>
          <p className="text-gray-600 mb-2">
            64 emociones únicas para la comunidad neurodivergente
          </p>
          <p className="text-sm text-gray-500">
            Desarrollado con 💙 por Manolo para el ecosistema ND
          </p>
        </footer>
      </div>
    </div>
  )
}

export default App

