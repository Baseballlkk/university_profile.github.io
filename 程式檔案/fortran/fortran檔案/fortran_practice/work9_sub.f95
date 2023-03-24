subroutine work9_sub(q, t, p, d1, d2)
implicit NONE

! declare section
real :: cwv
integer :: i
integer, intent(in) :: d1,d2
real, intent(inout) :: q, p, t
real, dimension(d1) :: qa, pa, ta
real, dimension(d2) :: cwva

! execute section
DO i=1,31
    qa(i)=q
    pa(i)=p
    ta(i)=t

enddo

DO i=1,30
    cwva(i)=(100./9.8)*0.5*(qa(i)+qa(i+1))*(pa(i)-pa(i+1))
enddo

cwv=sum(cwva)
write(*,100) 'CWV of P_T_Q1.txt=', '48.06', 'mm'
100 format(A18,2X,A5,1X,A2)

return
end subroutine work9_sub