program hw12
implicit none

! declare section
integer :: lrec, lrecma, lrecme
real, dimension(41,69,366) :: prec
real, dimension(41,69) :: maxprec
real, dimension(41,69) :: meanprec 

! execute section

! read data
INQUIRE(IOLENGTH=LREC) prec
open(unit=10, file='TCCIP_prec_2020.dat', form='unformatted', status='old', access='direct',recl=lrec)
read(10,rec=1) prec

! calculate for maximum precipitation
maxprec = max(prec)

! calculate for mean precipitation
meanprec = sum(prec)/366

! open file for maximum precipitation
INQUIRE(IOLENGTH=LRECme) meanprec
open(unit=20,file='prec_mean.dat',form='unformatted',access='direct',recl=lrecme)
write(20,rec=1) meanprec

! open file for mean precipitation
INQUIRE(IOLENGTH=LRECma) maxprec
open(unit=30,file='prec_max.dat',form='unformatted',access='direct',recl=lrecma)
write(30,rec=1) maxprec

! close file
close 10
close 20
close 30

end program hw12