!1970-2013年の8月のprecipの検定統計量Tと自由度mを求める
program test
    implicit none
    integer, parameter :: xdim = 2560, ydim = 3360
    integer :: ra(xdim, ydim)
    real*4 :: precip(xdim, ydim)

    open(11, file='/home/jjthomson/fdrive/ra/202007/01/202007010030.bin', form='unformatted', &
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

    open(20, file='/home/jjthomson/fdrive/ra/test.bin', form='unformatted', &
    & access='direct', recl=xdim*ydim*4)
    write(20,rec=1)

end program
