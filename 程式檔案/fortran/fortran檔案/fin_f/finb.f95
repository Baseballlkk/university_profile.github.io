program finb
implicit none

! declare section
integer, parameter :: NT=24
integer, dimension(NT) :: hr
real, dimension(NT) :: T, RH, Vs, THW
real :: e, und
integer :: i

! execute section

und=1.0E20
! open file
open(unit=10,file='OBS_20220103.txt',form='formatted',status='old')
read(10,*)

! initialize counter
i=0

! read data

do i=1,24
    read(10,100) hr(i), T(i), RH(i), Vs(i)
    100 format(I2,4X,F6.1,4x,F4.2,4X,F3.1)
end do

! calculate for THW
do i=1,24
    if ((T(i)>=-273.15).and.(0<=RH(i)).and.(RH(i)<=1).and.(Vs(i)>=0)) then
        if (T(i)>=0) then 
            e=6.11*RH(i)*exp((17.27*T(i))/(T(i)+237.3))
            THW(i) = 1.07*T(i)+0.2*e-0.65*Vs(i)-2.7
        else
            e=6.11*RH(i)*exp((21.875*T(i))/(T(i)+265.5))
            THW(i) = 1.07*T(i)+0.2*e-0.65*Vs(i)-2.7
    
        end if
    else
        THW=und    
    end if
end do

! output info
open(unit=20,file='finb.txt',form='formatted',status='replace')
write(20,300) 'Obs  THW (degC)'
300 format(A15)


do i=1,24
    write(20,200) hr(i), THW(i)
    200 format(I2,3X,E10.4e2)
enddo 

end program finb