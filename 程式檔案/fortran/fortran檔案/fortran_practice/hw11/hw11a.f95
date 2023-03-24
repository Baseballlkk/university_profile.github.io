program hw11a
implicit NONE

! declare section
character(33) :: headline
real, dimension(6) :: mean,means, max,maxs 
integer, dimension(6) :: count,counts, date,dates 
integer :: i
integer :: n=6


! execute section
open(unit=10,file='hw10a.txt',status='old')
read(10,100) headline
100 format(A33)

!  initialize
i=0

do i=1,6
    read(10,200) date(i), count(i), mean(i), max(i)
    200 format(I8,6X,I4,4X,F6.2,2X,F6.2)
    
ENDDO

dates=date
counts=count
means=mean
maxs=max

call sort(dates,counts,means,maxs,n)

open(unit=20,file='hw11a.txt',status='replace')
write(20,100) headline

DO i=1,6
    write(20,200) dates(i),counts(i),means(i),maxs(i)
enddo

end program hw11a