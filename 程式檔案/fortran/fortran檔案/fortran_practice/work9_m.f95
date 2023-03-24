program work9_m

! declare section
integer, parameter :: d1=31
integer, parameter :: d2=30
integer :: i



open(unit=10,,file='P_T_Q1.txt',STATUS='OLD')
READ(10,*)

do i=1,31
    read(10,*) p(i), t(i), q(i)
    call work9_sub(p(i),t(i),q(i),d1,d2)
enddo



end program work9_m