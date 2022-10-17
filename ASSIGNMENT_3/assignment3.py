import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

class VoltageData:
 """
 Classe per la misura di voltaggio prese ad un differente istante
 """

 def __init__(self, times, voltages):
  """
  
  """
  times = np.array(times, dtype = np.float64)
  voltages = np.array(voltages, dtype = np.float64)
  self.data = np.column_stack([times,voltages])
  self.spline = interpolate.InterpolatedUnivariateSpline(times, voltages, k=3)
# if len(self.time) != len(self.voltage):
#  raise ValueError('Tempo e Voltaggio non sono della stessa lunghezza!') 
 
 @classmethod #metodo di classe per leggere da file
 def from_file(cls, data_path):
  times, voltages = np.loadtxt(data_path, unpack = True)
  return cls(times, voltages)

 @property
 def times(self):
  return self.data[:,0]
 
 @property
 def voltages(self):
  return self.data[:,1]

 def __getitem__(self,index):
  return self.data[index]

 def __len__(self):
  return len(self.data)

 def __iter__(self):
  return iter(self.data)

 def __str__(self):
#  for row in enumerate(self):
#   output_str = ''
#   line = f'{i} -> {row[0]: 1f}, {row[1]: 2f}\n'
#   output_str += line
#  return output_str
  header = 'Row -> Time [s], Voltage [mV]\n'
  return header + '\n'.join([f'{i} -> {row[0]: 1f}, {row[1]: 2f}' \
    for i,row  in enumerate(self)])

 def __repr__(self):
  return '\n'.join([f'{row[0]}\t {row[1]}' for row  in self])

 def __call__(self, temp):
  return self.spline(temp)
  
 def plot(self, ax = None, draw_spline = False, **plot_opts):
  if ax is None:
   plt.figure('voltage VS time')
  else:
   plt.sca(ax)
  plt.plot(self.times, self.voltages, **plot_opts)
  if draw_spline:
   x = np.linspace(min(self.times), max(self.times),100)
   plt.plot(x, self(x), '-')
  plt.xlabel('Time[s]')
  plt.ylabel('Voltage[mV]')
  plt.grid(True)
   

if __name__ == '__main__':
 """
 """
 #t,v = np.loadtxt('sample_data_file.txt', unpack = True)
 vdata = VoltageData.from_file('sample_data_file.txt')

 print(repr(vdata))
 vdata.plot(color = 'k', marker = 'o', linestyle = '--', draw_spline = True)
 plt.show()