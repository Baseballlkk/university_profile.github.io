PROGRAM hw9a
IMPLICIT NONE

! SET time, WS,WD
CHARACTER(5) :: time
REAL :: WS, WD, pi, U, V, THETA
INTEGER :: i



! DO LOOP 
i = 0

DO i=1,4
    ! RECEIVE VALUE 
    WRITE(*,*) 'Please enter the time of data in [xx:xx]:'
    READ(*,*) time

    WRITE(*,*) 'Please enter the wind direction of data in [degree]:'
    READ(*,*) WD

    WRITE(*,*) 'Please enter the wind speed of data in [m/s]:'
    READ(*,*) WS

    ! CALCULATE U,V WIND
    pi = 4.*ATAN(1.)
    THETA = 270-WD

    U = WS*COS(THETA)
    V = WS*SIN(THETA)
    IF ((0<WD).AND.(WD<90)) THEN
        WRITE(*,*) 'At ',time,' (LST), the u-component of wind is ',U,' m/s, and the v-component of wind is ',V,' m/s, NE wind.'
    ELSEIF ((90<WD).AND.(WD<180)) THEN
        WRITE(*,*) 'At ',time,' (LST), the u-component of wind is ',U,' m/s, and the v-component of wind is ',V,' m/s, SE wind.'
    ELSEIF ((180<WD).AND.(WD<270)) THEN
        WRITE(*,*) 'At ',time,' (LST), the u-component of wind is ',U,' m/s, and the v-component of wind is ',V,' m/s, SW wind.'
    ELSEIF ((270<WD).AND.(WD<360)) THEN
        WRITE(*,*) 'At ',time,' (LST), the u-component of wind is ',U,' m/s, and the v-component of wind is ',V,' m/s, NW wind.'
    ENDIF
ENDDO

END PROGRAM hw9a