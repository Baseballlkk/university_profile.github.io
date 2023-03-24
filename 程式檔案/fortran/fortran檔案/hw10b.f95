PROGRAM hw10b
IMPLICIT NONE

! DECALRE SECTION
CHARACTER(33) :: HEAD
INTEGER :: i, j, k, l, maximumc
CHARACTER(8), DIMENSION(6) :: date, dates
INTEGER, DIMENSION(6) :: co, cots
REAL, DIMENSION(6) :: mean,means,ma, mas
REAL ::maximum,maximumm
CHARACTER(8) :: maximumd

! initialize
i=0
j=0
k=0
l=0

! CONDUCT SECTION
OPEN(UNIT=10,FILE='hw10a.txt',STATUS='OLD')
READ(10,100) HEAD
100 FORMAT(A33)

OPEN(UNIT=20,FILE='hw10b.txt',STATUS='REPLACE')
WRITE(20,*) HEAD
200 FORMAT(A8,6X,I4,4X,F6.2,2X,F6.2)

DO i=1,6
    READ(10,200) date(i), co(i), mean(i), ma(i)
END DO

means=mean
cots=co
dates=date
mas=ma
DO j=1,5
    k=j
    maximum=means(k)
    maximumd=dates(k)
    maximumc=cots(k)
    maximumm=mas(k)
    DO l=j+1,6
        IF (means(l) > maximum) THEN
            k=l
            maximum=means(k)
            maximumd=dates(k)
            maximumc=cots(k)
            maximumm=mas(k)
        END IF 
    END DO
    means(k)=means(j)
    dates(k)=dates(j)
    cots(k)=cots(j)
    mas(k)=mas(j)

    means(j)=maximum
    dates(j)=maximumd
    cots(j)=maximumc
    mas(j)=maximumm

WRITE(20,200) dates(j),cots(j),means(j),mas(j)
END DO




END PROGRAM hw10b