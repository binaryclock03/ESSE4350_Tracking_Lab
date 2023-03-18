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
    
    Real N "mean motion (km)";
    Real theta "true anomaly (deg)";
    Real E "Eccentric anomaly (deg";
    Real M "Mean anomaly (deg)";
    Real a "semi major (deg)";
    Real r "Sat radial distance (km)";
    Real P_sat_pf[3] "Position, Perifocal coords";
    Real v_sat_pf[3] "Velocity Peerifocal coords";
    
  initial equation
    N = N0 + (2*Ndot2/86400)*tstart + 3*Nddot6*tstart^2/86400^2;
    M = M0 + ((N*360.)/86400.)*tstart + Ndot2*tstart^2*360/86400^2 + Nddot6*tstart^3*360/86400^3;
  
  equation
    M*d2r = E*d2r - eccn*sin(E*d2r);
    tan(theta*d2r/2.) = sqrt((1 + eccn)/(1 - eccn))*tan(E*d2r/2.);
    a^3*(N*2*pi/86400.)^2 = 398600.4;
    der(M) = (N*360.)/86400. + 2.*Ndot2*time*360/86400^2 + 3.*Nddot6*time^2*360/86400^3;
    der(N) = 2*Ndot2/86400 + 6*Nddot6*time/86400^2;
    r = a*(1 - eccn^2)/(1 + eccn*cos(theta*d2r));
  
    P_sat_pf[1] = r*cos(theta*d2r);
    P_sat_pf[2] = r*sin(theta*d2r);
    P_sat_pf[3] = 0.;
    der(P_sat_pf[1]) = v_sat_pf[1];
    der(P_sat_pf[2]) = v_sat_pf[2];
    der(P_sat_pf[3]) = v_sat_pf[3];
  end Satellite;

  model GndStn
    constant Real d2r = Modelica.Constants.D2R "Degrees to radians";
  
    parameter Real stn_long "in deg";
    parameter Real stn_lat  "in deg";
    parameter Real stn_elev "km above sealevel";
    
    Real p_stn_ECF[3];
    
  protected
    constant Real eslr = 6378.137 "equatorial radius of sealevel";
    constant Real pslr = 6356.752 "polar radius of sealevel";
    
    Real radius;
    Real p;
    Real a;
    
  equation
    radius = eslr + stn_elev;
    p = stn_lat + 90;
    a = stn_long;
    
    p_stn_ECF[1] = radius * sin(p*d2r) * cos(a*d2r);
    p_stn_ECF[2] = radius * sin(p*d2r) * sin(a*d2r);
    p_stn_ECF[3] = radius * cos(p*d2r);
  end GndStn;

  function sat_PFtoECI "converts from periforcal to ECI coordinates"
    import Modelica.Mechanics.MultiBody.Frames.TransformationMatrices.axesRotations;
    import Modelica.Mechanics.MultiBody.Frames.TransformationMatrices.resolve2;
  
    input Real ang[3]  "argper, inc, raan";
    input Real p_PF[3] "pos in perifocal (km)";
    input Real v_PF[3] "vel in perifocal (km)";
    
    output Real p_ECI[3] "pos in ECI (km)";
    output Real v_ECI[3] "vel in ECI (km/2)";
  
  protected
    Real TM[3,3] = axesRotations(sequence={3,1,3}, angles=ang*d2r);
    constant Real d2r = Modelica.Constants.D2R "Degrees to radians";
  
  algorithm
    p_ECI := resolve2(TM, p_PF);
    v_ECI := resolve2(TM, v_PF);
  
  end sat_PFtoECI;

  function sat_ECItoECF
    import Modelica.Mechanics.MultiBody.Frames.TransformationMatrices.axesRotations;
    import Modelica.Mechanics.MultiBody.Frames.TransformationMatrices.resolve2;
  
    input Real ang "GMST angle (deg)";
    input Real p_ECI[3] "pos in ECI (km)";
    input Real v_ECI[3] "vel in ECI (km/s)";
    
    output Real p_ECF[3] "pos in ECF (km)";
    output Real v_ECF[3] "vel in ECF (km/s)";
  
  protected
    Real TM[3,3] = axesRotations(sequence={3,1,1}, angles={ang*d2r,0,0}); 
    constant Real d2r = Modelica.Constants.D2R "Degrees to radians";
  
  algorithm
    p_ECF := resolve2(TM, p_ECI);
    v_ECF := resolve2(TM, v_ECI);

  end sat_ECItoECF;

  function range_ECFtoTOPO
    import Modelica.Mechanics.MultiBody.Frames.TransformationMatrices.axesRotations;
    import Modelica.Mechanics.MultiBody.Frames.TransformationMatrices.resolve2;
    
    constant Real d2r = Modelica.Constants.D2R "Degrees to radians";
    
    input Real coords_stn[2] "lon, lat";
    input Real p_stn_ECF[3] "pos of stn in ECF coords";
    input Real p_sat_ECF[3] "pos of sat in ECF coords";
    input Real v_sat_ECF[3] "vel of sat in ECF coords";
    
    output Real p_sat_TOPO[3] "pos of sat in TOPO coords";
    output Real v_sat_TOPO[3] "vel of sat in TOPO coords";
    
  protected
    Real relative_ECF[3];
    Real TM[3,3] = axesRotation(sequence={2,3,2,1}, angles={-90*d2r, 90*d2r, coords_stn[1]*d2r, coords_stn[2]*d2r});
    
  algorithm
    relative_ECF := p_stn_ECF - p_sat_ECF;
    p_sat_TOPO := resolve2(TM, relative_ECF);
    v_sat_TOPO := resolve2(TM, v_sat_ECF);
    

  end range_ECFtoTOPO;

  function range_TOPOtoLA
    input Real p_sat_topo[3] "Position of satellite in topo coords (km)";
    input Real v_sat_topo[3] "Velocity of satellite in topo coords (km)";
  
    output Real Azimuth "Azimuth look angle (deg)";
    output Real Elevation "Elevation look angle (deg)";
    output Real Azrate "Azimuth look angle (deg/min)";
    output Real Elrate "Elevation look angle (deg/min)";
    output Real Rrate "Range rate to dish (km/s)";
  
  algorithm

  end range_TOPOtoLA;

  model Sat_Test
  Sattrak.Satellite MyTest(tstart = 64800., M0 = 263.2188, N0 = 2.00567916, eccn = .0007175, Ndot2 = -.00000014, Nddot6 = 0.);
    Real r "Sat radial distance (km)";
    Real theta "true anomaly (deg)";
    Real E "Eccentric anomaly (deg";
    Real M "Mean anomaly (deg)";
    
    Real p_PF[3];
    Real v_PF[3];
    
    Real p_ECI[3];
    Real v_ECI[3];
    
    Real p_ECF[3];
    Real v_ECF[3];
    
    //Real p_TOP[3];
    
    //inputs lol
    Real inc = 90;
    Real argper = 0;
    Real raan = 0;
  equation
    p_PF = MyTest.P_sat_pf;
    v_PF = MyTest.v_sat_pf;
    
    E = mod(MyTest.E, 360.);
    r = mod(MyTest.r, 360.);
    M = mod(MyTest.M, 360.);
    theta = mod(MyTest.theta, 360.);
    
    (p_ECI, v_ECI) = sat_PFtoECI(ang={argper,inc,raan}, p_PF = p_PF, v_PF = v_PF);
    
    (p_ECF, v_ECF) = sat_ECItoECF(ang=0, p_ECI=p_ECI, v_ECI=v_ECI);
    //p_ECF = sat_ECItoECF();
    
    annotation(
      Documentation(info "GPS BIII-6  (PRN 28)   
        1 55268U 23009A   23062.38276793 -.00000014  00000+0  00000+0 0  9992
        2 55268  55.0992 195.6677 0.007175 100.2205 263.2188  2.00567916  1141 https://celestrak.org/NORAD/elements/gp.php?GROUP=gps-ops&FORMAT=tle"),
      Icon);
  end Sat_Test;
end Sattrak;
