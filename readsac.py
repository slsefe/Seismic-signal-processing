#/usr/bin/python
import sys
import struct  


class sacfile_wave:  
  def read(self,sFile):  
          
  
        f=open(sFile,'rb')                  #以read方式打开string格式文件
        hdrBin=f.read(632)                  #读取632字节
          
        sfmt='f'*70+'I '*40+'8s '*22+'16s'  #4*70+4*40+8*22+16=632
        hdrFmt=struct.Struct(sfmt)          #
        self.m_header=hdrFmt.unpack(hdrBin) #将读取的632字节字节流转换成python数据类型（tuple）作为数据头部
          
        npts=int(self.m_header[79])         #数据点数
        delta=float(self.m_header[0])
        year=int(self.m_header[70])
        day=int(self.m_header[71])
        hour=int(self.m_header[72])
        minu=int(self.m_header[73])
        sec=int(self.m_header[74])
        msec=int(self.m_header[75])
        resp=float(self.m_header[21])       #灵敏度
        fmt_data='f'*npts                   #数据部分的字节数=数据点数*4
        dataFmt=struct.Struct(fmt_data)  
        dataBin=f.read(4*npts)              #读取数据部分
        f.close()  
        self.m_data=dataFmt.unpack(dataBin) #解析数据部分
        print "start time:year day hour minute sec msec:",year,day,hour,minu,sec,msec
        print "data len:",len(self.m_data)  
        print "sample",round(delta,2),"second and time length",npts*round(delta,2),"second"#样本时间和数据时间
        print "sensitivity for unit conversion",round(resp,2)   #单位换算灵敏度
        # round(flt, ndig),对flt四舍五入，保留ndig位小数
  def exportAsc(self,sAscFile):  
        f2=open(sAscFile,"wt")  
        sdataAsc=[str(x) for x in self.m_data]  #将数据转换为string形式
        sDataAsc='\n'.join(sdataAsc)            #换行，字符串拼接
        f2.writelines(sDataAsc)                 #以行为单位将数据全部写入到sAscFile文件
        f2.close()                              #关闭文件
      
if __name__=="__main__":  
    sacfile='XX.HSH.2008122000000.BHE'              #索引文件地址
    sac=sacfile_wave()                              #创建一个类
    sac.read(sacfile)                               #调用读方法读取文件
    sac.exportAsc("XX.HSH.2008122000000.BHE.asc")   #调动导出方法导出
