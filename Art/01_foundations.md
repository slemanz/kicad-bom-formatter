# 1. Foundations

There are two quantities that we like to keep track of in
electronic circuits: voltage and current. These are usually
changing with time; otherwise nothing interesting is hap-
pening.

- **Voltage** (symbol V or sometimes E). Ofﬁcially, the volt-
age between two points is the cost in energy (work done)
required to move a unit of positive charge from the more
negative point (lower potential) to the more positive
point (higher potential). Equivalently, it is the energy
released when a unit charge moves “downhill” from
the higher potential to the lower.2

- **Current** (symbol I). Current is the rate of ﬂow of elec-
tric charge past a point. The unit of measure is the
ampere, or amp, with currents usually expressed in
amperes (A),

The power (energy per unit time) consumed by a circuit
device is

$$ P = VI $$

This is simply (energy/charge) × (charge/time). For V in
volts and I in amps, P comes out in watts. A watt is a
joule per second (1W = 1 J/s).

### Relationship between voltage and current: resistors

Resistors (I simply proportional to V ),
capacitors (I proportional to rate of change of V ), diodes
(I ﬂows in only one direction), thermistors (temperature-
dependent resistor), photoresistors (light-dependent resis-
tor), strain gauges (strain-dependent resistor), etc.,

A resistor is made out of some conducting stuff (carbon,
or a thin metal or carbon ﬁlm, or wire of poor conductivity),
with a wire or contacts at each end.

The power dissipated by a resistor (or any other device) is
P = IV .

### Voltage sources and current sources

A real voltage source can supply
only a ﬁnite maximum current, and in addition it generally
behaves like a perfect voltage source with a small resis-
tance in series. Obviously, the smaller this series resistance,
the better.

Real current sources (a much-
neglected subject in most textbooks) have a limit to the
voltage they can provide (called the output-voltage compli-
ance, or just compliance), and in addition they do not pro-
vide absolutely constant output current. A current source
“likes” a short-circuit load and “hates” an open-circuit
load.

## Signals

Sinusoidal signals are the most popular signals around;
they’re what you get out of the wall plug. If someone says
something like “take a 10 μ V signal at 1 MHz,” they mean
a sinewave.

$$ V = A sin 2\pi f t $$

A linear circuit driven by
a sinewave always responds with a sinewave, although in
general the phase and amplitude are changed. No other pe-
riodic signal can make this statement. It is standard prac-
tice, in fact, to describe the behavior of a circuit by its fre-
quency response, by which we mean the way the circuit
alters the amplitude of an applied sinewave as a function
of frequency.

### Signal amplitudes and decibels

In addition to its amplitude, there are several other ways to
characterize the magnitude of a sinewave or any other sig-
nal. You sometimes see it speciﬁed by peak-to-peak ampli-
tude (pp amplitude), which is just what you would guess,
namely, twice the amplitude. The other method is to give
the root-mean-square amplitude (rms amplitude).

How do you compare the relative amplitudes of two sig-
nals? You could say, for instance, that signal X is twice
as large as signal Y . That’s ﬁne, and useful for many pur-
poses. But because we often deal with ratios as large as a
million, it is better to use a logarithmic measure, and for
this we present the decibel.

Although decibels are ordinarily used to specify the ra-
tio of two signals, they are sometimes used as an abso-
lute measure of amplitude. What is happening is that you
are assuming some reference signal level and expressing
any other level in decibels relative to it. There are sev-
eral standard levels (which are unstated, but understood)
that are used in this way; the most common references are
(a) 0 dBV (1 V rms); (b) 0 dBm (the voltage correspond-
ing to 1 mW into some assumed load impedance, which
for radiofrequencies is usually 50 Ω, but for audio is often
600 Ω; the corresponding 0 dBm amplitudes).

### Other signals