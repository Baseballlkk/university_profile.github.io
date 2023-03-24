subroutine sort(input, order, n, output neworder)
implicit NONE

! declare section
real, dimension(n), intent(in) :: input, order
integer, intent(in) :: n
real, dimension(n), intent(out) :: output, neworder
integer :: i, j, k
real :: maximum, maximumo

! execute section
output=input
neworder=order

! initialize
i=0
j=0
k=0

do i=1,n
    k=i
    maximum=output(k)
    maximum0=neworder(k)
    do j=i+1,n+1
        if (output(j)>maximum) then
            k=j
            maximum=output(k)
            maximumo=neworder(k)
        endif
    enddo
    output(k)=output(i)
    neworder(k)=neworder(i)

    output(i)=maximum
    neworder(i)=maximumo
enddo

return
end subroutine sort