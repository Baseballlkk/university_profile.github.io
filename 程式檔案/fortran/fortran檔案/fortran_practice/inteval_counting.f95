program interval_counting
implicit NONE

! decalre section
integer :: hour, minute, second

! execute section
write(*,*) 'input hour:'
read(*,*) hour

write(*,*) 'input minute:'
read(*,*) minute

write(*,*) 'input second:'
read(*,*) second

second = 3600*hour+60*minute+second

write(*,*) second

end program interval_counting