PROGRAM class2a
IMPLICIT NONE

! DECLARE T
REAL :: T, C


!INPUT T
WRITE(*,*) 'Please input temperature:'
READ(*,*) T

! compute c
C=T-273.15

If (T>=0.) THEN

    WRITE(*,*) C

ELSE 
    WRITE(*,*) 'T out of range'

ENDIF

END PROGRAM class2a