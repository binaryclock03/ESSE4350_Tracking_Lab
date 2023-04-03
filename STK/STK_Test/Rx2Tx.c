stk.v.12.0
WrittenBy    STK_v12.5.0

BEGIN Chain

    Name		 Rx2Tx
    BEGIN Definition
        Object		 Facility/Algonquin/Sensor/Dish/Receiver/LBand-Rx
        Object		 Constellation/Constellation1
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
            STKInst		 Facility/Algonquin/Sensor/Dish/Receiver/LBand-Rx
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
        END StrandObjIndexes

        SaveMode		 1
        BEGIN StrandAccessesByIndex
            Strand		 0 1
            Start		  0.0000000000000000e+00
            Stop		  1.8714204628847827e+04
            Start		  5.3731675703586945e+04
            Stop		  6.7069720447788146e+04
            Start		  8.4521983944755091e+04
            Stop		  8.6400000000000000e+04
            Strand		 0 2
            Start		  2.5436853926732034e+04
            Stop		  5.0860273866855961e+04
            Start		  7.3238739838620546e+04
            Stop		  7.9169913304231188e+04
            Strand		 0 3
            Start		  7.3874090480112600e+03
            Stop		  2.4100286848310214e+04
            Start		  5.9548954921867233e+04
            Stop		  7.7576258331029981e+04
            Strand		 0 4
            Start		  0.0000000000000000e+00
            Stop		  4.6714572306186238e+02
            Start		  1.8879136257546743e+04
            Stop		  3.0136444177294572e+04
            Start		  6.4575877528032608e+04
            Stop		  8.6400000000000000e+04
            Strand		 0 5
            Start		  2.2557500406627452e+04
            Stop		  4.8119818745449520e+04
            Start		  8.0926688426537265e+04
            Stop		  8.2726685576184056e+04
            Strand		 0 6
            Start		  8.9946041175431292e+03
            Stop		  3.4796425709054369e+04
            Start		  6.6419799084004786e+04
            Stop		  7.0084186743551822e+04
            Strand		 0 7
            Start		  0.0000000000000000e+00
            Stop		  1.1132031773972234e+04
            Start		  3.1898313420115493e+04
            Stop		  4.0014285361461698e+04
            Start		  7.3219594214491575e+04
            Stop		  8.6400000000000000e+04
            Strand		 0 8
            Start		  0.0000000000000000e+00
            Stop		  1.0712653089201036e+04
            Start		  4.4568199599686886e+04
            Stop		  5.3687495429251627e+04
            Start		  7.3796700693342660e+04
            Stop		  8.6400000000000000e+04
            Strand		 0 9
            Start		  0.0000000000000000e+00
            Stop		  3.3077369805330627e+03
            Start		  1.9730183972249164e+04
            Stop		  3.4320383992902032e+04
            Start		  6.9597220344212765e+04
            Stop		  8.6400000000000000e+04
            Strand		 0 10
            Start		  2.3706659457094620e+03
            Stop		  8.3900925198619771e+03
            Start		  4.0740568794108745e+04
            Stop		  6.5697809186466999e+04
            Strand		 0 11
            Start		  1.4286318678519399e+04
            Stop		  4.0860904820376571e+04
            Strand		 0 12
            Start		  1.5437304156314563e+04
            Stop		  3.4342342873038768e+04
            Start		  5.0511876796806813e+04
            Stop		  6.6064544987628455e+04
            Strand		 0 13
            Start		  0.0000000000000000e+00
            Stop		  1.1578682950205608e+04
            Start		  2.9164848725433807e+04
            Stop		  5.0125856096798867e+04
            Start		  8.5020301316875077e+04
            Stop		  8.6400000000000000e+04
            Strand		 0 14
            Start		  0.0000000000000000e+00
            Stop		  2.1676392414280683e+04
            Start		  4.6563964722979967e+04
            Stop		  4.9344202177403124e+04
            Start		  8.2431651932186287e+04
            Stop		  8.6400000000000000e+04
            Strand		 0 15
            Start		  2.5363193446286787e+03
            Stop		  9.0805894186316345e+03
            Start		  3.0927868159313559e+04
            Stop		  5.4582870350164339e+04
            Strand		 0 16
            Start		  0.0000000000000000e+00
            Stop		  2.8640207553084961e+03
            Start		  3.5851702568221168e+04
            Stop		  4.1588031994434685e+04
            Start		  6.4643631281519214e+04
            Stop		  8.6400000000000000e+04
            Strand		 0 17
            Start		  7.3996751664968190e+02
            Stop		  2.7768308902955334e+04
            Strand		 0 18
            Start		  3.2209566466640026e+04
            Stop		  5.5362635535864356e+04
            Start		  7.5349804917028814e+04
            Stop		  8.4648962811899488e+04
            Strand		 0 19
            Start		  4.9281178554433127e+03
            Stop		  3.1205935440640562e+04
            Strand		 0 20
            Start		  1.8644128111228267e+04
            Stop		  4.3878281062213769e+04
            Start		  7.7116298643641669e+04
            Stop		  8.0849161700648852e+04
            Strand		 0 21
            Start		  0.0000000000000000e+00
            Stop		  1.5558378028188084e+04
            Start		  5.0255104777945409e+04
            Stop		  6.5242643628762438e+04
            Start		  8.1606771260794747e+04
            Stop		  8.6400000000000000e+04
            Strand		 0 22
            Start		  3.5454548726227891e+04
            Stop		  6.1467726644607435e+04
            Strand		 0 23
            Start		  9.3357281463100699e+03
            Stop		  2.2540629411820606e+04
            Start		  3.9661009373021487e+04
            Stop		  6.0146666964200333e+04
            Strand		 0 24
            Start		  1.9580150187479965e+04
            Stop		  3.5967398225007433e+04
            Start		  5.1895065667090290e+04
            Stop		  7.0089213662356080e+04
            Strand		 0 25
            Start		  3.1319937534399935e+04
            Stop		  3.8783667417613884e+04
            Start		  5.9900554025062469e+04
            Stop		  8.3559278573705378e+04
            Strand		 0 26
            Start		  0.0000000000000000e+00
            Stop		  5.4652360684243413e+03
            Start		  4.0338200983381415e+04
            Stop		  5.2842162141932589e+04
            Start		  7.0638949305577771e+04
            Stop		  8.6400000000000000e+04
            Strand		 0 27
            Start		  2.4521211146844122e+04
            Stop		  4.5585156094477970e+04
            Start		  6.3126606087838685e+04
            Stop		  7.5899079002820217e+04
            Strand		 0 28
            Start		  0.0000000000000000e+00
            Stop		  1.5016475252801178e+04
            Start		  3.3080066489934849e+04
            Stop		  4.4576810056490845e+04
            Start		  7.9215636601093182e+04
            Stop		  8.6400000000000000e+04
            Strand		 0 29
            Start		  5.3846295308687266e+04
            Stop		  7.9774860052597971e+04
            Strand		 0 30
            Start		  4.5183907271302618e+04
            Stop		  7.1950735973403949e+04
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

                StaticColor		 #0000ff
                AnimationColor		 #ff0000
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

