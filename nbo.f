      IMPLICIT REAL*8(A-H,O-Z)
      PARAMETER (MM=1000)
      PARAMETER (MMS=MM*MM)
      COMMON/CARTB/XB(MM),YB(MM),ZB(MM),ALPB(MM),NTA(MM)
      COMMON/CARTA/XA(MM),YA(MM),ZA(MM),ALPA(MM),NTB(MM)
      COMMON/DIST/RABCS(MMS),RABS(MMS)
      COMMON/CONST/PI,XC,YC,ZC
      COMMON/NEW/XCT(MM),YCT(MM),ZCT(MM),CHA(MM)
      COMMON/CONTRAC/CONTRA(MM),CONTRB(MM)
      DIMENSION FNUCX(MM),FNUCY(MM),FNUCZ(MM),QR(MM)
      CHARACTER(LEN=80) SUBNAME,Q1,Q2,c80tmp,name1
      DIMENSION RHO(MM,MM),DM(MM),NBFA(MM),NBFB(MM),ANORM(MM)
      DIMENSION NST(MM),NPS(MM),NAS(MM),SCOF(MM),NPI(MM),CHS(MM)
      DIMENSION PIORBX(MM,MM),PIORBY(MM,MM),PIORBZ(MM,MM),CHPI(MM)
      DIMENSION PNUCX(MM),PNUCY(MM),PNUCZ(MM),SNUCX(MM),SNUCY(MM)
      DIMENSION SPCOF(MM),CA(MM),ALP(MM),NPTB(MM),COA(MM,MM),SNUCZ(MM)
      DIMENSION FX(MM,MM),FY(MM,MM),FZ(MM,MM),WFNMO(MM)
      DIMENSION NAOST(MM),NAOED(MM),FAOX(MM,MM),FAOY(MM,MM),FAOZ(MM,MM)
      COMMON/LABEL/NLC

***************************************************************************
**** THE FOLLOWING VARIABLE ARE USED IN THE PROGRMME***********************
********* NATOM -- THE ATOM NUMBER WHERE TO CALCULATE THE FORCE
********* NA -- TOTAL NUMBER OF ATOMS
              PI=4.0*ATAN(1.0)
**********THIS IS TO READ THE FILE NAME AND THE ATOM NUMBER (FORCE)  ******        
      OPEN(UNIT=5,FILE='info.dat',access="sequential")
       READ(5,*)name1

        OPEN(123,FILE=name1,access="sequential")
        CALL skiplines(123,2)
********************TO READ No ATOMS  BASIS FUNCTIONS ETC ************************        
        READ (123,'(55x,i9)')NA
*        WRITE(*,*)NA
        CALL loclabel(123,'independent')
        BACKSPACE 123
        READ(123,'(55x,i9)')NBF
        READ(123,'(55x,i9)')NBIF
        WRITE(*,*)'NUMBER OF BASIS FN (NBF)', NBF      
        WRITE(*,*)'NUMBER OF INd BASIS FN (NBIF)', NBF      
*        WRITE(*,*)NBF
**********TO READ THE NUCLEAR CHARGES**********************
        CALL  loclabel(123,'Nuclear charges')
        READ(123,*)
        READ(123,"(5(1PE16.8))") (CHA(I),I=1,NA)
*        WRITE(*,*)(CHA(I),I=1,NA)
**********TO READ THE CARTESIAN COORDINATES*******************
        CALL  loclabel(123,'Current')
        READ(123,*)
        READ(123,"(5(1PE16.8))") (XCT(I),YCT(I),ZCT(I),I=1,NA)

*************************************************************
*                                                           *    
*   THIS IS TO READ THE SHELL TYPES AND NO OF PRIMITIVES PER*
*    SHELL, ATOMS TO SHELL MAP                              *                   
*                                                           *    
*************************************************************
        CALL  loclabel(123,'Shell types')
        READ (123,'(55x,i9)')NS
*        WRITE(*,*) 'THIS IS THE STARTING'
        READ(123,*) (NST(I),I=1,NS)
*        WRITE(*,11) (NST(I),I=1,NS)
11      FORMAT('',I9)
*        WRITE(*,*) 'HEY! THIS IS FOR SHELL TYPES'
        READ(123,*)
        READ(123,*) (NPS(I),I=1,NS)
*        WRITE(*,11) (NPS(I),I=1,NS)
*        WRITE(*,*) 'HEY! THIS IS FOR Number of primitives per shell'
        READ(123,*)
        READ(123,*) (NAS(I),I=1,NS)
*        WRITE(*,11) (NAS(I),I=1,NS)
*        WRITE(*,*) 'HEY! THIS IS FOR Shell to atom map 
*************************************************************
*                                                           *    
* READING EXPONENTS AND CONTRACTION coefficients            *
*    BOTH S AND SP                                          *                   
*************************************************************    
 
        READ (123,'(55x,i9)')NEXPO
        READ(123,*) (ALP(I),I=1,Nexpo)
*        WRITE(*,12) (ALP(I),I=1,Nexpo)
*        WRITE(*,*) ' EXPONENTS ARE PRINTED '
12      FORMAT('',ES20.8E2)

        READ (123,*)
        READ(123,*) (SCOF(I),I=1,Nexpo)
*        WRITE(*,12) (SCOF(I),I=1,Nexpo)
*        WRITE(*,*) ' Contraction coefficients ARE PRINTED '
        READ (123,*)
        READ(123,*) (SPCOF(I),I=1,Nexpo)
*        WRITE(*,*) ' Contraction coefficients ARE PRINTED '
*        WRITE(*,12) (SPCOF(I),I=1,Nexpo)
*        WRITE(*,*) ' SP Contraction coefficients ARE PRINTED '
        
*********************************************************************
*////////////////////MO COEFFICIENTS////////////////////////////////*
*********************************************************************
*        OPEN(123,FILE=name1,access="sequential")
        CALL loclabel(123,'Alpha MO coefficients')
        READ(123,'(50x,i20)') NMOC
        READ(123,"(5(1PE16.8))") ((COA(I,J),J=1,NBF),I=1,NBIF)
        DO I=1,NBIF
!        DO J=1,NBF
!         write(*,1010) (x(i), i=1,50)
        WRITE(1001,*)'* ORBITAL 1 ',I
        WRITE(1001,222)(COA(I,J),J=1,NBF)
222     FORMAT(4ES19.12E2)        
!        ENDDO
        ENDDO
        END
**********************************************************MULTIWFN***************************************
        subroutine skiplines(id,nskip)
        integer id,nskip
        do i=1,nskip
        read(id,*)
        end do
        end subroutine
****************************************************************************************************************
        subroutine loclabel(nfileid,label)
        IMPLICIT REAL*8(A-H,O-Z)
        character*256 line
        CHARACTER(LEN=*) label
        COMMON/LABEL/NLC
        ln=1
10    read (nfileid, '(A)', end = 20) line
      NLC= index (line, label)
        if ( NLC .ne. 0) then
        BACKSPACE nfileid
        RETURN
       ENDIF
        ln=ln+1
       goto 10
20     continue
       end
**********************************************************************************
