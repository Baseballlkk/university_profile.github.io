PROGRAM hw9b
IMPLICIT NONE

! READ FILE
OPEN(UNIT=10,FILE='hw2_data.txt')
OPEN(UNIT=20,FILE='hw9b.txt',STATUS='NEW')

! SET VAR
CHARACTER(5), DIMENSION(24) :: time
REAL, DIMENSION(24) :: WS, WD, U, V
INTEGER :: i
REAL :: pi

i = 0

READ(10,*) time, WS, WD
WRITE(20,*) 'Time    WS[m/s]          WD[deg]          u[m/s]           v[m/s]'
! DO LOOP
DO i=2,25
    ! CALCULATE U,V WIND
    pi = 4.*ATAN(1.)
    THETA = (270-WD(i))*pi/180

    U(i) = WS*COS(THETA)
    V(i) = WS*SIN(THETA)
    
    WRITE(20,*) time(i), WS(i), WD(i), U(i), V(i)
ENDDO

END PROGRAM hw9b