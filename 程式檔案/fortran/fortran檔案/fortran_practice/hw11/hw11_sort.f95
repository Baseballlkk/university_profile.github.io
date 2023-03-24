subroutine sort(dates,counts,means,maxs,n)

! declare section
real, dimension(n), intent(inout) :: dates, counts,means,maxs
integer :: i, j, k
real :: maximumd, maximumc, maximumme, maximumma

! execute section
do i=1,6
    k=i
    maximumd=dates(k)
    maximumc=counts(k)
    maximumme=means(k)
    maximumma=maxs(k)
    do j=i+1,7
        if (means(j)>maximumme) then
            k=j
            maximumd=dates(k)
            maximumc=counts(k)
            maximumme=means(k)
            maximumma=maxs(k)
        endif
    enddo
    dates(k)=dates(i)
    counts(k)=counts(i)
    means(k)=means(i)
    maxs(k)=maxs(i)

    dates(i)=maximumd
    counts(i)=maximumc
    means(i)=maximumme
    maxs(i)=maximumma
enddo

return
end subroutine sort