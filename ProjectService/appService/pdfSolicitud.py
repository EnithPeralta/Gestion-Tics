from  fpdf import FPDF
from datetime import datetime

class Pdf(FPDF):
    def header(self):
        self.image('media/fotos/logo.png',10,8,33)
        self.set_font('Arial', '', 15) 
        self.ln()
        self.cell(60)
        self.cell(80,10,'MESA DE SERVICIOS CTPI-CAUCA',0,0,'C')
        self.ln()
        self.cell(60)
        self.cell(80,10,'REPORTE SOLICITUD',0,0,'C')
        self.ln(30)
        
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(30, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'L')     
    
    def mostrarDatos(self,solicitudes):
        self.cell(30,10,"Fecha:")
        fecha = datetime.now()
        self.cell(40,10,str(fecha.day)+ "/" + str(fecha.month) + "/" + str(fecha.year))
        self.ln()
        
        self.set_font("Arial","B",12)
        self.cell(50,10,"Instructor",1,0,'C')
        self.cell(50,10,"Solicitud",1,0,'C')
        self.cell(40,10,"Ambiente",1,0,'C')
        self.cell(50,10,"Fecha",1,0,'C')
        self.ln()
        
        fila=110
        self.set_font('Arial', '', 8)
        for s in solicitudes:
            self.cell(50,10,f"{s.usuario.first_name}{s.usuario.last_name}",1,0,'C')
            self.cell(50,10,s.descripcion,1,0,'L')
            self.cell(40,10,s.oficina.nombre,1,0,'C')
            self.cell(50,10,str(s.fechaHoraCreacion),1,0,'C')
            self.ln()
            fila +=4
        self.ln()
        self.set_font("Arial","B",12)
        self.cell(500,10,"__________________________________",0,0,'C')
        self.ln()
        self.cell(500,10,"Lider TIC CTPI",0,0,'C')
        