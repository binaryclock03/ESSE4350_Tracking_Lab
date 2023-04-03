stk.v.12.0
WrittenBy    STK_v12.5.0

BEGIN Chain

    Name		 Chain2
    BEGIN Definition
        Object		 Constellation/Constellation1
        Object		 Facility/Algonquin/Sensor/Dish/Receiver/LBand-Rx
        Type		 Chain
        FromOperator		 Or
        FromOrder		 1
        ToOperator		 Or
        ToOrder		 1
        Recompute		 Yes
        IntervalType		 0
        ComputeIntervalStart		 0
        ComputeIntervalStop		 86400
        ComputeIntervalPtr		
        BEGIN EVENTINTERVAL
            BEGIN Interval
                Start		 27 Mar 2023 16:00:00.000000000
                Stop		 28 Mar 2023 16:00:00.000000000
            END Interval
            IntervalState		 Explicit
        END EVENTINTERVAL

        ConstConstraintsByStrands		 Yes
        UseSaveIntervalFile		 No
        UseMinAngle		 No
        UseMaxAngle		 No
        UseMinLinkTime		 No
        LTDelayCriterion		 2
        TimeConvergence		 0.005
        AbsValueConvergence		 1e-14
        RelValueConvergence		 1e-08
        MaxTimeStep		 360
        MinTimeStep		 0.01
        UseLightTimeDelay		 Yes
        DetectEventsUsingSamplesOnly		 No
        UseLoadIntervalFile		 No
        AllowSameInstInStrands		 Yes
        KeepStrandsWithNoIntvls		 No
        BEGIN StrandObjIndexes
            STKInst		 Satellite/PRN_01_37753/Transmitter/GPSTx
            STKInst		 Satellite/PRN_02_28474/Transmitter/GPSTx1
            STKInst		 Satellite/PRN_03_40294/Transmitter/GPSTx2
            STKInst		 Satellite/PRN_04_43873/Transmitter/GPSTx3
            STKInst		 Satellite/PRN_05_35752/Transmitter/GPSTx4
            STKInst		 Satellite/PRN_06_39741/Transmitter/GPSTx5
            STKInst		 Satellite/PRN_07_32711/Transmitter/GPSTx6
            STKInst		 Satellite/PRN_08_40730/Transmitter/GPSTx7
            STKInst		 Satellite/PRN_09_40105/Transmitter/GPSTx8
            STKInst		 Satellite/PRN_10_41019/Transmitter/GPSTx9
            STKInst		 Satellite/PRN_11_48859/Transmitter/GPSTx10
            STKInst		 Satellite/PRN_12_29601/Transmitter/GPSTx11
            STKInst		 Satellite/PRN_13_24876/Transmitter/GPSTx12
            STKInst		 Satellite/PRN_14_46826/Transmitter/GPSTx13
            STKInst		 Satellite/PRN_15_32260/Transmitter/GPSTx14
            STKInst		 Satellite/PRN_16_27663/Transmitter/GPSTx15
            STKInst		 Satellite/PRN_17_28874/Transmitter/GPSTx16
            STKInst		 Satellite/PRN_18_44506/Transmitter/GPSTx17
            STKInst		 Satellite/PRN_19_28190/Transmitter/GPSTx18
            STKInst		 Satellite/PRN_20_26360/Transmitter/GPSTx19
            STKInst		 Satellite/PRN_21_27704/Transmitter/GPSTx20
            STKInst		 Satellite/PRN_23_45854/Transmitter/GPSTx21
            STKInst		 Satellite/PRN_24_38833/Transmitter/GPSTx22
            STKInst		 Satellite/PRN_25_36585/Transmitter/GPSTx23
            STKInst		 Satellite/PRN_26_40534/Transmitter/GPSTx24
            STKInst		 Satellite/PRN_27_39166/Transmitter/GPSTx25
            STKInst		 Satellite/PRN_29_32384/Transmitter/GPSTx26
            STKInst		 Satellite/PRN_30_39533/Transmitter/GPSTx27
            STKInst		 Satellite/PRN_31_29486/Transmitter/GPSTx28
            STKInst		 Satellite/PRN_32_41328/Transmitter/GPSTx29
            STKInst		 Facility/Algonquin/Sensor/Dish/Receiver/LBand-Rx
        END StrandObjIndexes

        SaveMode		 1
        BEGIN StrandAccessesByIndex
            Strand		 0 30
            Start		  0.0000000000000000e+00
            Stop		  1.8714118726205401e+04
            Start		  5.3731590779616912e+04
            Stop		  6.7069633777447583e+04
            Start		  8.4521898002569680e+04
            Stop		  8.6400000000000000e+04
            Strand		 1 30
            Start		  2.5436768177867765e+04
            Stop		  5.0860188606133095e+04
            Start		  7.3238652882886759e+04
            Stop		  7.9169825424030554e+04
            Strand		 2 30
            Start		  7.3873231301098085e+03
            Stop		  2.4100201010541081e+04
            Start		  5.9548869238667030e+04
            Stop		  7.7576167278756329e+04
            Strand		 3 30
            Start		  0.0000000000000000e+00
            Stop		  4.6705994645625964e+02
            Start		  1.8879050023359010e+04
            Stop		  3.0136358155422626e+04
            Start		  6.4575791238702695e+04
            Stop		  8.6400000000000000e+04
            Strand		 4 30
            Start		  2.2557414385270098e+04
            Stop		  4.8119732524243118e+04
            Start		  8.0926602805112328e+04
            Stop		  8.2726599881823917e+04
            Strand		 5 30
            Start		  8.9945183929196883e+03
            Stop		  3.4796344311270695e+04
            Start		  6.6419712823524533e+04
            Stop		  7.0084100428044054e+04
            Strand		 6 30
            Start		  0.0000000000000000e+00
            Stop		  1.1131947351529334e+04
            Start		  3.1898225974290122e+04
            Stop		  4.0014198199463637e+04
            Start		  7.3219506936911421e+04
            Stop		  8.6400000000000000e+04
            Strand		 7 30
            Start		  0.0000000000000000e+00
            Stop		  1.0712566466141929e+04
            Start		  4.4568113859906989e+04
            Stop		  5.3687408826584040e+04
            Start		  7.3796615219213694e+04
            Stop		  8.6400000000000000e+04
            Strand		 8 30
            Start		  0.0000000000000000e+00
            Stop		  3.3076509774619190e+03
            Start		  1.9730097857775341e+04
            Stop		  3.4320298141197563e+04
            Start		  6.9597134343684360e+04
            Stop		  8.6400000000000000e+04
            Strand		 9 30
            Start		  2.3705791500699061e+03
            Stop		  8.3900060267013978e+03
            Start		  4.0740486856167132e+04
            Stop		  6.5697724007071505e+04
            Strand		 10 30
            Start		  1.4286232654739097e+04
            Stop		  4.0860818920118043e+04
            Strand		 11 30
            Start		  1.5437218821122669e+04
            Stop		  3.4342251605085388e+04
            Start		  5.0511790785135854e+04
            Stop		  6.6064459586597004e+04
            Strand		 12 30
            Start		  0.0000000000000000e+00
            Stop		  1.1578596625282413e+04
            Start		  2.9164758049277018e+04
            Stop		  5.0125770064784003e+04
            Start		  8.5020215837182550e+04
            Stop		  8.6400000000000000e+04
            Strand		 13 30
            Start		  0.0000000000000000e+00
            Stop		  2.1676306696719799e+04
            Start		  4.6563878533098185e+04
            Stop		  4.9344116075671482e+04
            Start		  8.2431570390213805e+04
            Stop		  8.6400000000000000e+04
            Strand		 14 30
            Start		  2.5362345674161070e+03
            Stop		  9.0805037664005686e+03
            Start		  3.0927781860947056e+04
            Stop		  5.4582784241547517e+04
            Strand		 15 30
            Start		  0.0000000000000000e+00
            Stop		  2.8639340386938688e+03
            Start		  3.5851617438789472e+04
            Stop		  4.1587946004383753e+04
            Start		  6.4643545515248836e+04
            Stop		  8.6400000000000000e+04
            Strand		 16 30
            Start		  7.3988698855240466e+02
            Stop		  2.7768223216641003e+04
            Strand		 17 30
            Start		  3.2209480161613661e+04
            Stop		  5.5362549854873469e+04
            Start		  7.5349718658131271e+04
            Stop		  8.4648876812993243e+04
            Strand		 18 30
            Start		  4.9280311972446125e+03
            Stop		  3.1205849723221796e+04
            Strand		 19 30
            Start		  1.8644041898524265e+04
            Stop		  4.3878195449899271e+04
            Start		  7.7116212481684604e+04
            Stop		  8.0849075766672919e+04
            Strand		 20 30
            Start		  0.0000000000000000e+00
            Stop		  1.5558289695862682e+04
            Start		  5.0255017892362426e+04
            Stop		  6.5242556342237061e+04
            Start		  8.1606687510322226e+04
            Stop		  8.6400000000000000e+04
            Strand		 21 30
            Start		  3.5454462463151751e+04
            Stop		  6.1467640964174818e+04
            Strand		 22 30
            Start		  9.3356432684839274e+03
            Stop		  2.2540542630285410e+04
            Start		  3.9660923452027419e+04
            Stop		  6.0146581040407975e+04
            Strand		 23 30
            Start		  1.9580065112224594e+04
            Stop		  3.5967311512346852e+04
            Start		  5.1894979693132627e+04
            Stop		  7.0089128045769350e+04
            Strand		 24 30
            Start		  3.1319856440133633e+04
            Stop		  3.8783581063599479e+04
            Start		  5.9900468376504665e+04
            Stop		  8.3559192061484355e+04
            Strand		 25 30
            Start		  0.0000000000000000e+00
            Stop		  5.4651498436035490e+03
            Start		  4.0338115835124139e+04
            Stop		  5.2842075439865876e+04
            Start		  7.0638863600442899e+04
            Stop		  8.6400000000000000e+04
            Strand		 26 30
            Start		  2.4521125051504270e+04
            Stop		  4.5585070206574397e+04
            Start		  6.3126519943470812e+04
            Stop		  7.5898993117398888e+04
            Strand		 27 30
            Start		  0.0000000000000000e+00
            Stop		  1.5016389908538898e+04
            Start		  3.3079979927667293e+04
            Stop		  4.4576723829294453e+04
            Start		  7.9215545196162668e+04
            Stop		  8.6400000000000000e+04
            Strand		 28 30
            Start		  5.3846209797910116e+04
            Stop		  7.9774773204842480e+04
            Strand		 29 30
            Start		  4.5183821062657167e+04
            Stop		  7.1950650604891634e+04
        END StrandAccessesByIndex


    END Definition

    BEGIN Extensions

        BEGIN ExternData
        END ExternData

        BEGIN ADFFileData
        END ADFFileData

        BEGIN Desc
        END Desc

        BEGIN Crdn
        END Crdn

        BEGIN Graphics

            BEGIN Attributes

                StaticColor		 #ffffff
                AnimationColor		 #00ff00
                AnimationLineWidth		 2
                StaticLineWidth		 3

            END Attributes

            BEGIN Graphics
                ShowGfx		 On
                ShowStatic		 Off
                ShowAnimationHighlight		 On
                ShowAnimationLine		 On
                ShowLinkDirection		 Off
            END Graphics
        END Graphics

        BEGIN VO
        END VO

    END Extensions

END Chain

