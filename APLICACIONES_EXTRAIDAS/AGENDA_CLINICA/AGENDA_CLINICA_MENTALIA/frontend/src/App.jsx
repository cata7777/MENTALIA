import { useState, useEffect } from 'react'
import { Button } from '@/components/ui/button.jsx'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card.jsx'
import { Badge } from '@/components/ui/badge.jsx'
import { Progress } from '@/components/ui/progress.jsx'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs.jsx'
import { Calendar, Users, Clock, FileText, Activity, Phone, Video, Stethoscope } from 'lucide-react'
import './App.css'

function App() {
  const [isConnected, setIsConnected] = useState(false)
  const [todayAppointments, setTodayAppointments] = useState([])

  useEffect(() => {
    // Verificar conexión con backend
    fetch('http://localhost:5003/api/health')
      .then(res => res.json())
      .then(data => {
        setIsConnected(true)
        console.log('Conectado a Agenda Clínica Backend:', data)
      })
      .catch(err => {
        console.log('Backend no disponible:', err)
        setIsConnected(false)
      })

    // Datos de ejemplo para citas de hoy
    setTodayAppointments([
      {
        id: 1,
        patient: 'Ana García',
        time: '09:00',
        type: 'Evaluación TDAH',
        status: 'Confirmada',
        mode: 'Presencial'
      },
      {
        id: 2,
        patient: 'Carlos Mendoza',
        time: '10:30',
        type: 'Seguimiento Autismo',
        status: 'En curso',
        mode: 'Telemedicina'
      },
      {
        id: 3,
        patient: 'María López',
        time: '14:00',
        type: 'Terapia Cognitiva',
        status: 'Pendiente',
        mode: 'Presencial'
      }
    ])
  }, [])

  const stats = [
    {
      title: 'Citas Hoy',
      value: '8',
      icon: <Calendar className="h-5 w-5" />,
      color: 'text-blue-600'
    },
    {
      title: 'Pacientes Activos',
      value: '156',
      icon: <Users className="h-5 w-5" />,
      color: 'text-green-600'
    },
    {
      title: 'Tiempo Promedio',
      value: '45min',
      icon: <Clock className="h-5 w-5" />,
      color: 'text-purple-600'
    },
    {
      title: 'Reportes Pendientes',
      value: '12',
      icon: <FileText className="h-5 w-5" />,
      color: 'text-orange-600'
    }
  ]

  const features = [
    {
      title: 'Gestión de Pacientes',
      description: 'Historiales clínicos neurodivergentes',
      icon: <Users className="h-6 w-6" />
    },
    {
      title: 'Agenda Inteligente',
      description: 'Programación automática optimizada',
      icon: <Calendar className="h-6 w-6" />
    },
    {
      title: 'Telemedicina',
      description: 'Consultas virtuales integradas',
      icon: <Video className="h-6 w-6" />
    },
    {
      title: 'Reportes Clínicos',
      description: 'Documentación automática',
      icon: <FileText className="h-6 w-6" />
    }
  ]

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-green-50 to-purple-50">
      {/* Header */}
      <header className="bg-white/80 backdrop-blur-sm border-b border-blue-200 sticky top-0 z-50">
        <div className="container mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-3">
              <div className="w-10 h-10 bg-gradient-to-r from-blue-600 to-green-600 rounded-lg flex items-center justify-center">
                <Stethoscope className="h-6 w-6 text-white" />
              </div>
              <div>
                <h1 className="text-2xl font-bold bg-gradient-to-r from-blue-600 to-green-600 bg-clip-text text-transparent">
                  Agenda Clínica ND
                </h1>
                <p className="text-sm text-gray-600">Sistema Interoperable Neurodivergente</p>
              </div>
            </div>
            <div className="flex items-center space-x-2">
              <Badge variant={isConnected ? "default" : "destructive"}>
                {isConnected ? "Conectado" : "Desconectado"}
              </Badge>
              <Button className="bg-gradient-to-r from-blue-600 to-green-600 hover:from-blue-700 hover:to-green-700">
                Nueva Cita
              </Button>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="container mx-auto px-4 py-8">
        <Tabs defaultValue="dashboard" className="space-y-6">
          <TabsList className="grid w-full grid-cols-6">
            <TabsTrigger value="dashboard">Dashboard</TabsTrigger>
            <TabsTrigger value="appointments">Citas</TabsTrigger>
            <TabsTrigger value="patients">Pacientes</TabsTrigger>
            <TabsTrigger value="reports">Reportes</TabsTrigger>
            <TabsTrigger value="telemedicine">Telemedicina</TabsTrigger>
            <TabsTrigger value="settings">Configuración</TabsTrigger>
          </TabsList>

          {/* Dashboard Tab */}
          <TabsContent value="dashboard" className="space-y-6">
            {/* Stats Cards */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
              {stats.map((stat, index) => (
                <Card key={index} className="hover:shadow-lg transition-shadow">
                  <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                    <CardTitle className="text-sm font-medium">{stat.title}</CardTitle>
                    <div className={stat.color}>{stat.icon}</div>
                  </CardHeader>
                  <CardContent>
                    <div className="text-2xl font-bold">{stat.value}</div>
                  </CardContent>
                </Card>
              ))}
            </div>

            {/* Today's Appointments */}
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center space-x-2">
                  <Calendar className="h-5 w-5" />
                  <span>Citas de Hoy</span>
                </CardTitle>
                <CardDescription>
                  Agenda del día actual con pacientes neurodivergentes
                </CardDescription>
              </CardHeader>
              <CardContent>
                <div className="space-y-4">
                  {todayAppointments.map((appointment) => (
                    <div key={appointment.id} className="flex items-center justify-between p-4 border rounded-lg hover:bg-gray-50">
                      <div className="flex items-center space-x-4">
                        <div className="w-2 h-2 rounded-full bg-blue-500"></div>
                        <div>
                          <div className="font-semibold">{appointment.patient}</div>
                          <div className="text-sm text-gray-600">{appointment.type}</div>
                        </div>
                      </div>
                      <div className="flex items-center space-x-4">
                        <Badge variant="outline">{appointment.mode}</Badge>
                        <Badge variant={appointment.status === 'Confirmada' ? 'default' : 
                                      appointment.status === 'En curso' ? 'secondary' : 'outline'}>
                          {appointment.status}
                        </Badge>
                        <div className="text-sm font-medium">{appointment.time}</div>
                      </div>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>

            {/* Features Grid */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
              {features.map((feature, index) => (
                <Card key={index} className="hover:shadow-lg transition-shadow cursor-pointer">
                  <CardHeader className="text-center">
                    <div className="mx-auto w-12 h-12 bg-gradient-to-r from-blue-100 to-green-100 rounded-lg flex items-center justify-center mb-2">
                      {feature.icon}
                    </div>
                    <CardTitle className="text-lg">{feature.title}</CardTitle>
                    <CardDescription>{feature.description}</CardDescription>
                  </CardHeader>
                </Card>
              ))}
            </div>
          </TabsContent>

          {/* Appointments Tab */}
          <TabsContent value="appointments" className="space-y-6">
            <Card>
              <CardHeader>
                <CardTitle>Gestión de Citas</CardTitle>
                <CardDescription>
                  Programación y seguimiento de citas médicas
                </CardDescription>
              </CardHeader>
              <CardContent>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                  <Button className="h-20 flex flex-col items-center justify-center">
                    <Calendar className="h-6 w-6 mb-2" />
                    Nueva Cita
                  </Button>
                  <Button variant="outline" className="h-20 flex flex-col items-center justify-center">
                    <Clock className="h-6 w-6 mb-2" />
                    Ver Agenda
                  </Button>
                  <Button variant="outline" className="h-20 flex flex-col items-center justify-center">
                    <Activity className="h-6 w-6 mb-2" />
                    Seguimiento
                  </Button>
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          {/* Patients Tab */}
          <TabsContent value="patients" className="space-y-6">
            <Card>
              <CardHeader>
                <CardTitle>Gestión de Pacientes</CardTitle>
                <CardDescription>
                  Historiales clínicos y perfiles neurodivergentes
                </CardDescription>
              </CardHeader>
              <CardContent>
                <div className="space-y-4">
                  <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                    <div className="p-4 border rounded-lg hover:bg-gray-50">
                      <h3 className="font-semibold">Pacientes TDAH</h3>
                      <p className="text-sm text-gray-600">45 pacientes activos</p>
                      <Badge className="mt-2">Activo</Badge>
                    </div>
                    <div className="p-4 border rounded-lg hover:bg-gray-50">
                      <h3 className="font-semibold">Pacientes TEA</h3>
                      <p className="text-sm text-gray-600">32 pacientes activos</p>
                      <Badge className="mt-2">Activo</Badge>
                    </div>
                    <div className="p-4 border rounded-lg hover:bg-gray-50">
                      <h3 className="font-semibold">Otros Neurotipos</h3>
                      <p className="text-sm text-gray-600">79 pacientes activos</p>
                      <Badge className="mt-2">Activo</Badge>
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          {/* Reports Tab */}
          <TabsContent value="reports" className="space-y-6">
            <Card>
              <CardHeader>
                <CardTitle>Reportes Clínicos</CardTitle>
                <CardDescription>
                  Documentación automática y análisis de datos
                </CardDescription>
              </CardHeader>
              <CardContent>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div className="p-4 border rounded-lg">
                    <h3 className="font-semibold">Reportes Mensuales</h3>
                    <p className="text-sm text-gray-600 mt-2">Estadísticas de atención</p>
                    <Button className="mt-3" size="sm">Generar</Button>
                  </div>
                  <div className="p-4 border rounded-lg">
                    <h3 className="font-semibold">Análisis de Progreso</h3>
                    <p className="text-sm text-gray-600 mt-2">Evolución de pacientes</p>
                    <Button className="mt-3" size="sm">Ver Análisis</Button>
                  </div>
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          {/* Telemedicine Tab */}
          <TabsContent value="telemedicine" className="space-y-6">
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center space-x-2">
                  <Video className="h-5 w-5" />
                  <span>Telemedicina</span>
                </CardTitle>
                <CardDescription>
                  Consultas virtuales y seguimiento remoto
                </CardDescription>
              </CardHeader>
              <CardContent>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div className="text-center p-6 border rounded-lg">
                    <Video className="h-12 w-12 mx-auto mb-4 text-blue-600" />
                    <h3 className="font-semibold mb-2">Consulta Virtual</h3>
                    <Button>Iniciar Videollamada</Button>
                  </div>
                  <div className="text-center p-6 border rounded-lg">
                    <Phone className="h-12 w-12 mx-auto mb-4 text-green-600" />
                    <h3 className="font-semibold mb-2">Consulta Telefónica</h3>
                    <Button variant="outline">Iniciar Llamada</Button>
                  </div>
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          {/* Settings Tab */}
          <TabsContent value="settings" className="space-y-6">
            <Card>
              <CardHeader>
                <CardTitle>Configuración del Sistema</CardTitle>
                <CardDescription>
                  Personalización y ajustes de la agenda clínica
                </CardDescription>
              </CardHeader>
              <CardContent>
                <div className="space-y-4">
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div className="p-4 border rounded-lg">
                      <h3 className="font-semibold">Horarios de Atención</h3>
                      <p className="text-sm text-gray-600">Configurar disponibilidad</p>
                    </div>
                    <div className="p-4 border rounded-lg">
                      <h3 className="font-semibold">Tipos de Consulta</h3>
                      <p className="text-sm text-gray-600">Personalizar servicios</p>
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>
          </TabsContent>
        </Tabs>
      </main>

      {/* Footer */}
      <footer className="bg-white/80 backdrop-blur-sm border-t border-blue-200 mt-12">
        <div className="container mx-auto px-4 py-6">
          <div className="text-center text-sm text-gray-600">
            <p>Agenda Clínica Interoperable ND | Sistema de Gestión Neurodivergente 2026</p>
            <p className="mt-1">Stack: React + JavaScript/Node.js + Hyperfoco | Diseño editable</p>
          </div>
        </div>
      </footer>
    </div>
  )
}

export default App

