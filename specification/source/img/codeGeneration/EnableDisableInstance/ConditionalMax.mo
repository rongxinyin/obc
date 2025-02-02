block ConditionalMax
  "Maximum between two inputs, of which one input can be conditionally removed"
  parameter Boolean u2_present = true "If true, input u2 is present";
  CDL.Interfaces.RealInput u1 "Real input";
  CDL.Interfaces.RealInput u2 if u2_present "Real input";
  CDL.Interfaces.RealOutput y "Real output";
protected
  CDL.Interfaces.RealInput u_internal
    "Internal input needed to connect to conditional connector";
equation
  connect(u_internal, u2);
  if not u2_present then
    u_internal = 0;
  end if;
  y = if u2_present then max(u1, u_internal) else u1;
end ConditionalMax;
