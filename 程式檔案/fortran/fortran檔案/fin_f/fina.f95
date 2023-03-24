program fina
implicit none

! declare section
real :: T, RH, Vs, e, THW, und

! execute section

und=1.0E20

! read input data
write(*,*) 'Input temperature in degree Celsius, relative humidity, and windspeed in m/s:'
read(*,*) T, RH,Vs

! calculate for THW
if ((T>=-273.15).and.(0<=RH).and.(RH<=1).and.(Vs>=0)) then
    if (T>=0) then 
        e=6.11*RH*exp((17.27*T)/(T+237.3))
        THW = 1.07*T+0.2*e-0.65*Vs-2.7
    else
        e=6.11*RH*exp((21.875*T)/(T+265.5))
        THW = 1.07*T+0.2*e-0.65*Vs-2.7
    
    end if
else
    THW=und    
end if

! output info
write(*,*) 'Temperature = ',T,' degree Celsius'
write(*,*) 'Relative Humidity = ',100.*RH,' %'
write(*,*) 'Wind Speed = ',Vs,' m/s'
write(*,*) 'THW Index = ',THW,' degre Celsius'

end program fina