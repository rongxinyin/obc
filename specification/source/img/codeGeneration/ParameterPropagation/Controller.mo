block Controller "Controller with time sampling"
  ...
  parameter Modelica.SIunits.Time samplePeriod=120
    "Sample period of component";
  ...
  OBC.ASHRAE.G36_PR1.AHUs.MultiZone.VAV.SetPoints.SupplyFan
    supFan(final samplePeriod=samplePeriod) "Supply fan controller";
  ...
equation
  ...
end Controller;
