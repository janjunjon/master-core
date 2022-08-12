program test
    implicit none
    integer, parameter :: xdim = 2560, ydim = 3360
    integer(kind=2) :: ra(xdim, ydim)
    real(kind=4) :: precip(xdim, ydim)
    integer :: i, j, k, y, m, d, t

    open(11, file='/root/fdrive/ra/202007/01/202007010030.bin', form='unformatted', &
    & access='direct', recl=xdim*ydim*2)

        !初期値を与える
        do j=1, ydim
            do i=1, xdim
                precip(i,j)=0
            end do
        end do

        do m=1,xdim*ydim
            read(11,rec=m) ra
            do j=1, ydim
                do i=1, xdim
                    precip(i,j)= ra(i,j)/10
                end do
            end do
        end do


    write(*,*) precip

    open(20, file='/root/fdrive/ra/converted/202007010030_converted.bin', form='unformatted', &
    & access='direct', recl=xdim*ydim*4)
    write(20,rec=1)

end program
