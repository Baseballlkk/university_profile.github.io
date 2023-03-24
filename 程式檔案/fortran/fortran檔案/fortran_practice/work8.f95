program work8
implicit NONE

! declare section
real :: cwv
integer :: i
real, dimension(31) :: q, p, t
real, dimension(30) :: cwv1

! execute section
open(unit=10,file='P_T_Q1.txt',STATUS='OLD')
READ(10,*) 

do i=1,31
    read(10,*) p(i), t(i), q(i)
enddo

DO i=1,30
    cwv1(i)=(100./9.8)*0.5*(q(i)+q(i+1))*(p(i)-p(i+1))
enddo

cwv = sum(cwv1)
write(*,100) 'CWV of P_T_Q1.txt=', CWV, 'mm'
100 format(A18,2X,F5.2,1X,A2)

end program work8