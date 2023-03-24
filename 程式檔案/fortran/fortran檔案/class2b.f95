PROGRAM class2b
IMPLICIT NONE

! DECLARE T
INTEGER :: i
REAL :: T, C

! COMPUTE C
i=3


! DO LOOP
DO i=1,5
    WRITE(*,*) 'input temperature:'
    READ(*,*) T
    IF (T>=0) THEN
        C = T-273.15
        WRITE(*,*) i, C
    ELSE
        WRITE(*,*) i,'T out of range'
    
    ENDIF
ENDDO

END PROGRAM class2b