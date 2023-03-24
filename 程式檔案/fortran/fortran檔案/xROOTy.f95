FUNCTION xROOTy(x,y)
IMPLICIT NONE

! DECLARE SECTION
REAL :: xROOTy
REAL, intent(in) :: x,y

! executing section

xROOTy = x**y

return
END FUNCTION xROOTy