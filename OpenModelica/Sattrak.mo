package Sattrak
    model Satellite
    constant Real pi = Modelica.Constants.pi;
    constant Real d2r = Modelica.Constants.D2R "Degrees to radians";
    parameter Real eccn "Eccentricity";
    parameter Real M0 "Mean anomaly at Epoch (deg)";
    parameter Real N0 "Mean motion at Epoch (rev/d)";
    parameter Real Ndot2 "1st der Mean Motion /2 rev/d^2";
    parameter Real Nddot6 "2nd der Mean Motion /6 rev/d^3";
    parameter Real tstart "Simulation start time, seconds";
    parameter Real i "inclination in deg";
    parameter Real RAAN0 " RAAN at start time in deg";
    parameter Real w0 "argument of perigee at start time in deg";
    parameter Real J2=1.081874e-03 "J2 perturbation";
    parameter Real Re= 6378.135 " Earth radius (km)";
    Real N "mean motion (rev/day)";
    Real theta "true anomaly (deg)";
    Real E "Eccentric anomaly (deg";
    Real M "Mean anomaly (deg)";
    Real a "semi major (deg)";
    Real r "Sat radial distance (km)";
    
    Real p_sat_pf[3] "Position, Perifocal coords";
    Real v_sat_pf[3] "Velocity Peerifocal coords";
    
    Real RAAN "RAAN in deg";
    Real w "argument of perigee deg";
    
    Real Ang_P2ECI[3]" angles between perifocal and ECI in (rad)";
    //    Real Ang_ECI2ECF[1] "Angle between ECI to ECF"
  initial equation
    N = N0 + (2*Ndot2/86400)*tstart + 3*Nddot6*tstart^2/86400^2;
    M = M0 + ((N*360.)/86400.)*tstart + Ndot2*tstart^2*360/86400^2 + Nddot6*tstart^3*360/86400^3;
    
    RAAN=RAAN0 +(-(((3*(J2)*((Re)^2)*cos(i))/(2*(a^2)*(1-eccn^2)^2))*((N*360.)/86400.)))*(time-tstart);
    w=w0 +((3*(J2)*((Re)^2)*(5*cos(i)^2-1))/(2*(a^2)*(1-eccn^2)^2))*((N*360.)/86400.)*(time-tstart);
equation
    M*d2r = E*d2r - eccn*sin(E*d2r);
    tan(theta*d2r/2.) = sqrt((1 + eccn)/(1 - eccn))*tan(E*d2r/2.);
    a^3*(N*2*pi/86400.)^2 = 398600.4;
    der(M) = (N*360.)/86400. + 2.*Ndot2*time*360/86400^2 + 3.*Nddot6*time^2*360/86400^3;
    der(N) = 2*Ndot2/86400 + 6*Nddot6*time/86400^2;
    r = a*(1 - eccn^2)/(1 + eccn*cos(theta*d2r));
    
    p_sat_pf[1] = r*cos(theta*d2r);
    p_sat_pf[2] = r*sin(theta*d2r);
    p_sat_pf[3] = 0.;
    der(p_sat_pf[1]) = v_sat_pf[1];
    der(p_sat_pf[2]) = v_sat_pf[2];
    der(p_sat_pf[3]) = v_sat_pf[3];
    
    der(RAAN)=-((3*(J2)*((Re)^2)*cos(i))/(2*(a^2)*(1-eccn^2)^2))*((N*360.)/86400.);
    der(w)=((3*(J2)*((Re)^2)*(5*cos(i)^2-1))/(2*(a^2)*(1-eccn^2)^2))*((N*360.)/86400.);
    
    Ang_P2ECI[1]=-w*d2r;
    Ang_P2ECI[2]=-i*d2r;
    Ang_P2ECI[3]=-RAAN*d2r;
    
    
    
  end Satellite;

  model Sat_Test
    Sattrak.Satellite MyTest(tstart=26131., M0=41.2839 , N0=2.00563995, eccn=.0066173, Ndot2= 0, Nddot6=0., i=55.5538, RAAN0=144.8123, w0=51.6039);
   //ARO coords
    Sattrak.GndStn GndTest(stn_long=281.9269597222222 ,stn_lat=45.95550333333333 ,stn_elev=0.26042,Frequency=1575.42);
     
  //Sattrak.Visibility VisTest(Azimuth1=Azimuth,Elevation1=Elevation,Azrate1=Azrate,Elrate1=Elrate,ElMinTable= 9.0, ElMaxTable=89);
    Real r "Sat radial distance (km)";
    Real theta "true anomaly (deg)";
    Real E "Eccentric anomaly (deg";
    Real M "Mean anomaly (deg)";
    
    Real p_sat_ECI[3] "position of sat in ECI (Km)";
    Real v_sat_ECI[3] "velocity of sat in ECI (km/s)";
    Real p_sat_ECF[3] "position of sat in ECF (Km)";
    Real v_sat_ECF[3] "velocity of sat in ECF (km/s)";
    Real p_sat_topo[3]"Position of satellite relative to station, topo coords (km)";
    Real v_sat_topo[3]"Velocity of satellite relative to station, topo coords(km/s)";
    Real p_stn_ECF[3];
    
     Real Azimuth "Azimuth look angle (deg)";
     Real Elevation "Elevation look angle (deg)";
     Real Azrate "Azimuth look angle (deg/min)";
     Real Elrate "Elevation look angle (deg/min)";
     Real Rrate  "Range rate to dish (km/s)";
  
    Real doppler " the value of the doppler shift";
    Boolean InView;
    Boolean TooFast;
    
    Real AOS;
    Real LOS;
    
    Boolean Trackable;
    Boolean Not_Trackable;
  
  Real ElMin = 9;
  Real ElMax = 89;
  Real Elrate_max = 10;
  Real Azrate_max = 10;
    
    
    Real days = 8483;
    Real hours =time/3600;
    Real GMST;
   
  //Real AOS;
  //Real LOS;
  equation
    GMST = theta_d(days, hours); // calculate GMST angle
    E= mod(MyTest.E, 360.);
    r= mod(MyTest.r, 360.);
    M= mod(MyTest.M, 360.);
    theta= mod(MyTest.theta, 360.);
    
   (p_sat_ECI,v_sat_ECI)=sat_ECI(ang=MyTest.Ang_P2ECI,p_sat_pf=MyTest.p_sat_pf,v_sat_pf=MyTest.v_sat_pf);//sat_ECI test
   (p_sat_ECF,v_sat_ECF)=sat_ECF(ang=GMST, p_sat_ECI=p_sat_ECI, v_sat_ECI=v_sat_ECI); // sat_ECF test
   
   (p_sat_topo, v_sat_topo) = Range_ECF2topo(p_stn_ECF=GndTest.p_stn_ECF, p_sat_ECF=p_sat_ECF, v_sat_ECF=v_sat_ECF, TM=GndTest.TM);   // Range_ECF2topo test
   
   p_stn_ECF=GndTest.p_stn_ECF;
   
  (Azimuth,Elevation,Azrate,Elrate,Rrate)= Range_topo2look_angles(stn_long=GndTest.stn_long, stn_lat=GndTest.stn_lat, stn_elev=GndTest.stn_elev, p_sat_topo=p_sat_topo, v_sat_topo=v_sat_topo); // Range_topo2look_angles test
  
  
    InView = Elevation >= ElMin and Elevation <=  ElMax;
    TooFast = abs(Elrate) >= Elrate_max and abs(Azrate) >= Azrate_max;
    
    Trackable = InView and not(TooFast);
    Not_Trackable = not(Trackable);
  //Booleans for trackability
  // Equations for AOS, LOS
    if initial() then
      AOS = if InView then time else -1.;
      LOS=-1;
    end if;
  
  
  
  when {edge(Trackable)} then
      AOS = time;
  end when;
    //Other conditions for LOS
  when {edge(Not_Trackable)} then
      LOS = time;
  end when;
  
  doppler=(Rrate/300000)*GndTest.Frequency;
  
  
  
    annotation(
    Documentation(info "GPS BIIR-2  (PRN 13)    
  1 24876C 97035A   23081.69756944  .00000000  00000+0  00000+0 0   815
  2 24876  55.5538 144.8123 0066173  51.6039  41.2839  2.00563995    17 https://celestrak.org/NORAD/elements/gp.php?GROUP=gps-ops&FORMAT=tle"),
          Icon);
  end Sat_Test;

  model GndStn
   constant Real d2r = Modelica.Constants.D2R "Degrees to radians";
   parameter Real stn_long "Station longitude (degE)";
   parameter Real stn_lat "Station latitude (degN)";
   parameter Real stn_elev "Station elevation (km)";
   
   parameter Real Frequency "frequency of ground station dish (MHz)";
   Real f "Earth reference ellipsoid flattening";
   Real e "ellipsoidal eccentricity";
   Real p_stn_ECF[3] "Station coordinates in ECF (km)";
   Real TM[3,3] "Transform matrix from ECF to topo";
   Real Re=6378.137 "earth radius km";
   Real a[3] "1st row of TM";
   Real b[3] "2nd row of TM";
   Real c[3] "3rd row of TM";
   Real N_lat "Earth ellipsoidal radius of curvature of the meridian";
  equation
  f= 1/298.25223563;
  e=sqrt((2*f)-(f^2));
  
  a= {-sin(stn_long*d2r),cos(stn_long*d2r),0} "first row";
  
  b={-cos(stn_long*d2r)*sin(stn_lat*d2r), -sin(stn_long*d2r)*sin(stn_lat*d2r),cos(stn_lat*d2r)} "Second row";
  
  c={cos(stn_long*d2r)*cos(stn_lat*d2r), sin(stn_long*d2r)*cos(stn_lat*d2r),sin(stn_lat*d2r)} "third row";
  
  
   N_lat = Re/sqrt(1-((e^2)*(sin(stn_lat*d2r))^2))"Earth ellipsoidal radius of curvature of the meridian";
   TM[1,1:3]=a;
   TM[2,1:3]=b;
   TM[3,1:3]=c;
   
   p_stn_ECF={(N_lat + stn_elev)*cos(stn_lat*d2r)*cos(stn_long*d2r),(N_lat + stn_elev)*cos(stn_lat*d2r)*sin(stn_long*d2r),((1-e^2)*N_lat + stn_elev)*sin(stn_lat*d2r)} "ECF cartesian coordinates of tracking station";
  end GndStn;

  function sat_ECI"Converts Peri-focal coordinates to ECI"
  
  import Modelica.Mechanics.MultiBody.Frames.TransformationMatrices.axesRotations;
  import Modelica.Mechanics.MultiBody.Frames.TransformationMatrices.resolve2;
   input Real ang[3] "-argper, -inc, -raan (rad)";
   input Real p_sat_pf[3] "Posn vector in Perifocal coords (km)";
   input Real v_sat_pf[3] "Velocity vector in Perifocal coords (km/s)";
   
   output Real p_sat_ECI[3] "Posn vector in ECI coords (km)";
   output Real v_sat_ECI[3] "Velocity vector in ECI coords (km/s)";
   
  protected
   Real TM[3,3]=axesRotations(sequence={3, 1, 3},angles=ang);
    
  algorithm
  
   p_sat_ECI:= resolve2(TM,p_sat_pf );
   v_sat_ECI:= resolve2(TM,v_sat_pf );
  end sat_ECI;

  function sat_ECF"Converts ECI to ECF coordinates"
   import Modelica.Mechanics.MultiBody.Frames.TransformationMatrices.axesRotations;
  import Modelica.Mechanics.MultiBody.Frames.TransformationMatrices.resolve2;
  
  
   input Real ang "GMST angle (deg)";
   input Real p_sat_ECI[3] "Position vector in ECI coordinates (km)";
   input Real v_sat_ECI[3] "Velocity vector in ECI coordinates (km/s)";
   
   output Real p_sat_ECF[3] "Position vector in ECF coordinates (km)";
   output Real v_sat_ECF[3] "Relative Velocity vector in ECF coordinates (km/s)";
   
   protected
   
  Real v_ECI_a[3];
  Real v_ECI_b[3];
  constant Real pi = Modelica.Constants.pi;
  constant Real d2r = Modelica.Constants.D2R "Degrees to radians";
  
  Real cross[3,3] = skew({0., 0., 360./86164. *d2r}) " used to convert to side real days";
  Real TM1[3,3] = axesRotations(sequence={3, 1, 3}, angles={ang*d2r, 0, 0});
  
  algorithm
  p_sat_ECF:= resolve2(TM1,p_sat_ECI );
  v_ECI_a := resolve2(TM1,v_sat_ECI);
  v_ECI_b := v_ECI_a-cross*p_sat_ECF;
  v_sat_ECF:= resolve2(TM1,v_ECI_b);
  //v_ECF:= resolve2(TM1,v_ECI );
  
  end sat_ECF;

  function Range_ECF2topo
  import Modelica.Mechanics.MultiBody.Frames.TransformationMatrices.resolve2;
  
   input Real p_stn_ECF[3] "Position of station in ECF coords";
   input Real p_sat_ECF[3] "Position of satellite in ECF coords";
   input Real v_sat_ECF[3] "Relative Velocity of satellite in ECF coords";
   input Real TM[3, 3] "Transform matrix from ECF to topo";
   output Real p_sat_topo[3] "Position of satellite relative to station, topo coords (km)";
   output Real v_sat_topo[3] "Velocity of satellite relative to station, topo coords 
  (km/s)";
  
  algorithm
p_sat_topo := resolve2(TM,p_sat_ECF-p_stn_ECF)"compute pos of sat relative to topoECF";
  v_sat_topo := resolve2(TM,v_sat_ECF)"compute vel of sat relative to topoECF";
  
  end Range_ECF2topo;

  function Range_topo2look_angles
  import Modelica.Mechanics.MultiBody.Frames.TransformationMatrices.axesRotations;
  import Modelica.Mechanics.MultiBody.Frames.TransformationMatrices.resolve2;
  import Modelica.Math.atan;
   input Real stn_long "Station longitude (degE)";
   input Real stn_lat "Station latitude (degN)";
   input Real stn_elev "Station elevation (m)";
   input Real p_sat_topo[3] "Position of satellite in topo coords (km)";
   input Real v_sat_topo[3] "Velocity of satellite in topo coords (km)";
   
   output Real Azimuth "Azimuth look angle (deg)";
   output Real Elevation "Elevation look angle (deg)";
   output Real Azrate "Azimuth look angle (deg/min)";
   output Real Elrate "Elevation look angle (deg/min)";
   output Real Rrate "Range rate to dish (km/s)";
  protected 
//Real TM[3,3] ={p_sat_topo[1] +T[1],p_sat_topo[2] +T[2],p_sat_topo[3] +T[3]}"ECF to topo coord";
  Real R =sqrt((p_sat_topo[1]^2) + (p_sat_topo[2]^2) + (p_sat_topo[3]^2)) "Calculate range";
  Real R_r= (p_sat_topo[1] * v_sat_topo[1] + p_sat_topo[2] * v_sat_topo[2]+ p_sat_topo[3]* v_sat_topo[3])/R "range rate to dish";
  
  Real Az = atan(p_sat_topo[1]/p_sat_topo[2])*180/Modelica.Constants.pi "Azimuth look angle (deg)";
  Real Azr =(p_sat_topo[2]*v_sat_topo[1]-p_sat_topo[1]*v_sat_topo[2])/(sqrt((p_sat_topo[1]^2) +(p_sat_topo[2]^2)))^2"Azimuth look angle rate (deg/min)";
  
  Real El = atan(p_sat_topo[3]/(sqrt(p_sat_topo[1]^2 +p_sat_topo[2]^2)))*180/Modelica.Constants.pi "Elevation look angle (deg)";
  Real Elr =(sqrt((p_sat_topo[1]^2) + (p_sat_topo[2]^2))*v_sat_topo[3]-((p_sat_topo[3])/sqrt((p_sat_topo[1]^2) + (p_sat_topo[2]^2)))*(p_sat_topo[1]*v_sat_topo[1]+p_sat_topo[2]*v_sat_topo[2]))*(1/sqrt((p_sat_topo[1]^2) + (p_sat_topo[2]^2)+(p_sat_topo[3]^2))^2)"Elevation look angle rate (deg/min)"; 
  algorithm
 Azimuth :=Az;
   Elevation := El;
   Azrate :=Azr;
   Elrate :=Elr; 
   Rrate :=R_r;
  end Range_topo2look_angles;

  function theta_d"Calculates GMST angle"
   input Real days "Number of days from J2000 to start of day in question";
   input Real hours "hours from midnight of the day in question to time in 
  question";
   output Real GMST "GMST angle (deg)";
   protected
   Real D_u = days-0.5;
   Real tmid = -0.5;
   Real Tu = D_u/36525.;
   Real GMSTh = 24110.5484+8640184.*Tu+0.093104*Tu^2-6.2e-6*Tu^3;
   Real GMST_Mod=mod(GMSTh,86400);
   
   Real theta_mid= 360*GMST_Mod/86400;
   Real rTu = 1.002737909350795+5.9006e-11*Tu-5.9e-15*Tu^2;
   
   
   
  algorithm
  GMST := mod(theta_mid + 360*rTu*((hours/24)), 360);
  end theta_d;

  model RisingEdge
    Boolean u;
    Integer i;
    Real Elmin;
    Real ELmax;
    parameter Real x; // current elevation
    parameter Real EL_Range[2]; //elevation range of dish [1] is min [2] is max
  equation
    Elmin =EL_Range[1];
    Elmax =EL_Range[2];
    u = x > Elmin and x < Elmax;
    when edge(u) then
      i = pre(i) + 1;
    end when;
  end RisingEdge;

  model Visibility
    import Modelica.Math.Vectors.interpolate;
   Sattrak.Satellite MyTest(tstart=26131., M0=41.2839 , N0=2.00563995, eccn=.0066173, Ndot2= 0, Nddot6=0., i=55.5538, RAAN0=144.8123, w0=51.6039);
   Sattrak.GndStn GndTest(stn_long=281.9269597222222 ,stn_lat=45.95550333333333 ,stn_elev=0.26042);
   
    Real p_sat_ECI[3] "Posn vector in ECI coords (km)";
    Real v_sat_ECI[3] "Velocity vector in ECI coords (km/s)";
    Real p_sat_ECF[3];
    Real v_sat_ECF[3]; 
    Real p_sat_topo[3];
    Real v_sat_topo[3]; 
    Real Azimuth "Azimuth look angle (deg)";
    Real Elevation "Elevation look angle (deg)";
    Real Azrate "Azimuth look angle (deg/min)";
    Real Elrate "Elevation look angle (deg/min)";
    Real Rrate "sat range rate (km/sec)";
    Real Elrate_max= 10;
    Real AZrate_max=10;
   Real GMST;
   Real ElMin " smallest elevation angle";
   Real ElMax " largest eleavation angle";
   Real Elmins =9 " smallest elevation angle";
   Real Elmaxs = 89 " largest eleavation angle";
  
  Real hours;
  Real days;
  Boolean InView;
  Real time;
  //time of event Acquisition/Loss of signal (sec)
  Real AOS;
  Real LOS;
  
  Boolean Trackable;
  Boolean N_View;
  Boolean Fast;
  Boolean N_Fast;
  
  equation
    // Bring in or calculate Azimuth and Elevation angles and rates
   (p_sat_ECI,v_sat_ECI)=sat_ECI(ang=MyTest.Ang_P2ECI,p_sat_pf=MyTest.p_sat_pf,v_sat_pf=MyTest.v_sat_pf);//sat_ECI test
   
   GMST = theta_d(days, hours); // calculate GMST angle
   
   (p_sat_ECF,v_sat_ECF)=sat_ECF(ang=GMST, p_sat_ECI=p_sat_ECI, v_sat_ECI=v_sat_ECI); // sat_ECF test
   
   (p_sat_topo, v_sat_topo) = Range_ECF2topo(p_stn_ECF=GndTest.p_stn_ECF, p_sat_ECF=p_sat_ECF, v_sat_ECF=v_sat_ECF, TM=GndTest.TM);   // Range_ECF2topo test
   
   (Azimuth,Elevation,Azrate,Elrate,Rrate)= Range_topo2look_angles(stn_long=GndTest.stn_long, stn_lat=GndTest.stn_lat, stn_elev=GndTest.stn_elev, p_sat_topo=p_sat_topo, v_sat_topo=v_sat_topo); // Range_topo2look_angles test
  
  //Interpolate to get elevation angles
   
    // Boolean expressions for visibility
    if InView == (Elevation >= ElMin and Elevation <= ElMax) then
       InView = true;
    end if;
    N_View= Elevation <=ElMin or Elevation >= ElMax;
    Fast = Elrate >= Elrate_max or Elrate<=-Elrate_max or Azrate >= Azrate_max or Azrate <=-Azrate-max;
    N_Fast= Elrate <= Elrate_max and Elrate>=-Elrate_max and Azrate <= Azrate_max and Azrate >=-Azrate-max;
  //Booleans for trackability
  //Trackable = Azrate <= 10 and Elrate <=10;
  // Equations for AOS, LOS
    if initial() then
      AOS = if InView and Trackable then time else -1.;
      LOS=-1;
    end if;
    
    
  when {edge(InView and Trackable) } then
      AOS = time;
  end when;
    //Other conditions for LOS
  when {edge(not InView or not Trackable)} then
      LOS = time;
  end when;
    
  end Visibility;
end Sattrak;
