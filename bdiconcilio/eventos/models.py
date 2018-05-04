from django.db import models
from datetime import datetime


# Create your models here.
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
#import uuid

class Evento(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    #id=models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name='Codigo')
    nombre = models.CharField(max_length=80, help_text='Entre el nombre del evento')
    descripcion = models.TextField(max_length=256, help_text='Entre una descripcion breve del evento')
    tarifa = models.DecimalField(max_digits=8, decimal_places=2)
    duracion = models.DurationField(default=0)
    imagen = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    promo = models.ForeignKey('Promocion', on_delete=models.SET_NULL, null=True)
       
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.nombre   


class Promocion(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name='Codigo')
    ciclo = models.CharField(max_length=50, help_text='Entre nombre del ciclo del evento')
    fecha_inicio = models.DateField(default=datetime.today)
    fecha_fin = models.DateField(default=datetime.today)
    fecha_cierre = models.DateField(default=datetime.today)
    
    class Meta:
        ordering = ["fecha_inicio"]
        
    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0} ({1})'.format(self.id,self.ciclo)
        
    
class FechaEvento(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    evento = models.ForeignKey('Evento', on_delete=models.SET_NULL, null=True)
    fecha = models.DateField(default=datetime.today)
    hora_inicio = models.DurationField()
    hora_final = models.DurationField()
    
    class Meta:
        ordering = ["fecha"]
        
    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0} ({1})'.format(self.id,self.evento_id)
        
    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this book.
        """
        return reverse('evento-detalle', args=[str(self.evento.id)])

class Exposicion(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    evento = models.ForeignKey('Evento', on_delete=models.SET_NULL, null=True)
    expositor = models.ForeignKey('Expositor', on_delete=models.SET_NULL, null=True)
    localidad = models.ForeignKey('Localidad', on_delete=models.SET_NULL, null=True)
    cap_minima = models.IntegerField(default=0, verbose_name='Capacidad Minima' )
    cap_maxima = models.IntegerField(default=0, verbose_name='Capacidad Maxima' )
            
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.id

class Expositor(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    cedula = models.CharField(max_length=11, help_text='Entre su cedula')
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.CharField(max_length=256)
    correo = models.EmailField()
    fecha = models.DateField(auto_now_add=True)
    tarifa = models.DecimalField(max_digits=8, decimal_places=2)
    EXPO_ESTADO = (
        ('a', 'activo'),
        ('i', 'inactivo'),
        
    )
    estado = models.CharField(max_length=1, choices=EXPO_ESTADO, blank=True, default='a', help_text='Estado del expositivo')
            
    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0}, {1}, {2}'.format(self.apellido, self.nombre)
        
    
class Localidad(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name='Codigo')
    nombre = models.CharField(max_length=50)
    edificio = models.CharField(max_length=50)
    salon = models.CharField(max_length=50)
    capacidad = models.IntegerField(default=0, verbose_name="Capacidad de Asistentes" )
            
    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0}, {1}, {2}, {3}'.format(self.nombre, self.edificio, self.salon, self.capacidad)

class Participante(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name='Codigo')
    cedula = models.CharField(max_length=11, help_text='Entre su cedula')
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.CharField(max_length=120)
    correo = models.EmailField()
    telefono = models.CharField(max_length=10)
                
    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0}, {1}'.format(self.apellido, self.nombre)

class Registro(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name='Codigo')
    evento = models.ForeignKey('Evento', on_delete=models.SET_NULL, null=True)
    agente_pago = models.ForeignKey('AgentePago', on_delete=models.SET_NULL, null=True)
    participante  = models.ForeignKey('Participante', on_delete=models.SET_NULL, null=True)
    fecha = models.DateField(default=datetime.today, editable=False)
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0}, {1}'.format(self.evento.nombre, self.participante.nombre)
        
class AgentePago(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name='Codigo')
    cedula = models.CharField(max_length=11, help_text='Entre su cedula')
    nombre = models.CharField(max_length=60)
    telefono = models.CharField(max_length=10)
    contacto = models.CharField(max_length=60)
    direccion = models.CharField(max_length=120)
    correo = models.EmailField()
                 
    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0}, {1}'.format(self.cedula, self.nombre)        

class Recibo(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name='Recibo Numero')
    agente_pago = models.ForeignKey('AgentePago', on_delete=models.SET_NULL, null=True)
    registro = models.ForeignKey('Registro', on_delete=models.SET_NULL, null=True)
    referencia = models.CharField(max_length=50)
    nota = models.TextField(max_length=256)
    fecha = models.DateField(default=datetime.today, editable=False)
    #total = Registro.objects.annotate(amount=Sum('total')).order_by('-fecha')
    
    #total = models.DecimalField((max_digits=10, decimal_places=2))
                 
    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0}, {1}'.format(self.agente_pago.cedula, self.agente_pago.nombre)        

        
