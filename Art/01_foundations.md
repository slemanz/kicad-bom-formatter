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

- **Ramp:** The ramp is a signal that is simply a voltage rising (or falling) at a
constant rate.

- **Triangle:**  The triangle wave is a close cousin of the ramp; it is simply
a symmetrical ramp.

- **Noise:** Signals of interest are often mixed with noise.
- 
- **Square wave:** A square wave is a signal that varies in time like
the sinewave, it is characterized by amplitude and frequency (and perhaps phase).
The edges of a square wave are not perfectly square; in
typical electronic circuits the rise time tr ranges from a few
nanoseconds to a few microseconds.

- **Pulses:** A pulse is a signal that is deﬁned by amplitude and pulse width. You
can generate a train of periodic (equally spaced) pulses, in
which case you can talk about the frequency, or pulse repe-
tition rate, and the “duty cycle,” the ratio of pulse width to
repetition period (duty cycle ranges from zero to 100%).

- **Steps and spikes:**  Steps and spikes are signals that are talked about a lot but
are not so often used. They provide a nice way of describing what happens in a circuit.

Pulses and square waves are used extensively in digital electronics, in which predeﬁned voltage levels represent
one of two possible states present at any point in the circuit. These states are called simply HIGH and LOW, and
correspond to the 1 (true) and 0 (false) states of Boolean logic.

Often the source of a signal is some part of the circuit you are working on. But for test purposes a ﬂexible sig-
nal source is invaluable. They come in three ﬂavors: signal generators, pulse generators, and function generators.

## Capacitors and ac circuits

Once we enter the world of changing voltages and currents, or “signals,” we encounter two very interesting circuit
elements that are useless in purely dc circuits: capacitors and inductors. As you will see, these humble devices,
combined with resistors, complete the triad of passive linear circuit elements that form the basis of nearly all
circuitry. 

Capacitors are used for waveform generation, ﬁltering, and blocking and bypass applications.

Is a device that has two wires sticking out of it and has the property

$$ Q = CV $$

Its basic form is a pair of closely-spaced metal plates, separated by some insulating material, as in the rolled-
up “axial-ﬁlm capacitor”.

Emphasize those ﬁrst two applications – bypass and coupling – because they are the most common
uses of capacitors, and they are easy to understand at the simplest level.

Because a capacitor looks like an open circuit at dc, it lets you couple a varying signal while blocking its average dc
level. This is a blocking capacitor (also called a coupling capacitor)

Likewise, because a capacitor looks like a short circuit at high frequencies, it suppresses (“bypasses”)
signals where you don’t want them,

So a capacitor is more complicated than a resistor: the current is not simply proportional to the voltage, but rather
to the rate of change of voltage. If you change the voltage across a farad by 1 volt per second, you are supplying an
amp.

When you charge up a capacitor, you’re supplying energy. The capacitor doesn’t get hot; instead, it stores the
energy in its internal electric ﬁelds.

### RC circuits: V and I versus time

When dealing with ac circuits (or, in general, any circuits that have changing voltages and currents), there are two
possible approaches. You can talk about V and I versus time, or you can talk about amplitude versus signal frequency.
Both approaches have their merits, and you ﬁnd yourself switching back and forth according to which description
is most convenient in each situation.

The product RC is called the time constant of the circuit. For R in ohms and C in farads, the product RC is in seconds.
A microfarad across 1.0k has a time constant of 1 ms; if the capacitor is initially charged to 1.0 V, the initial current
is 1.0 mA.

Eventually (when t >> RC), V reaches Vf . (Presenting the “5RC rule of thumb”: a capacitor charges or decays to
within 1% of its ﬁnal value in ﬁve time constants).

### Unintentional capacitive coupling

Differentiators sometimes crop up unexpectedly, in situations where they’re not welcome.

Real capacitors (the kind you can see, and touch, and pay money for) generally behave according to theory; but they
have some additional “features” that can cause problems in some demanding applications. For example, all capacitors
exhibit some series resistance (which may be a function of frequency), and some series inductance.

along with some frequency-dependent parallel resistance. Then there’s a “memory” effect (known as dielectric
absorption), which is rarely discussed in polite society: if you charge a capacitor up to some voltage V0 and hold it
there for a while, and then discharge it to 0 V, then when you remove the short across its terminals it will tend to
drift back a bit toward V0 .

## Inductors and transformers

They’re closely related to capacitors: the rate of current change in an inductor
is proportional to the voltage applied across it.

Putting a constant voltage across an inductor causes the current to rise as a ramp (compare with
a capacitor, in which a constant current causes the voltage to rise as a ramp).

Inductors let you do neat tricks, such as increasing a and decreasing dc input voltage.

A transformer is a device consisting of two closely coupled coils (called primary and secondary). An ac voltage applied
to the primary appears across the secondary, with a voltage multiplication proportional to the turns ratio of the
transformer, and with a current multiplication inversely proportional to the turns ratio. **Power is conserved.**

## Diodes and diode circuits

The diode is an important and useful two-terminal passive nonlinear device.

### Rectiﬁcation

A rectiﬁer changes ac to dc; this is one of the simplest and most important applications of diodes (which are some-
times called rectiﬁers).

The preceding rectiﬁed waveforms aren’t good for much as they stand. They’re “dc” only in the sense that they don’t
change polarity. But they still have a lot of “ripple” (periodic variations in voltage about the steady value) that has
to be smoothed out in order to generate genuine dc. This we do by attaching a relatively large value capacitor

**Rectiﬁer conﬁgurations for power supplies:**

- Full-wave bridge: In practice, you generally buy the bridge as a prepackaged module. The smallest ones
come with maximum current ratings of 1 A average.

- Center-tapped full-wave rectiﬁer: The output voltage is half what you get if you use a bridge rectiﬁer. It is not the
most efﬁcient circuit in terms of transformer design, because each half of the secondary is used only half the time.

### Other diodes circuits

**Split supply:** It gives you split supplies (equal plus and minus voltages), which many circuits need. It is an
efﬁcient circuit, because both halves of the input waveform are used in each winding section.

**Voltage multipliers:** Think of it as two half-wave rectiﬁer circuits in series. It is ofﬁcially a full-wave rectiﬁer circuit because both
halves of the input waveform are used – the ripple frequency is twice the ac frequency. Variations of this circuit 
exist for voltage triplers, quadruplers, etc.

## Regulators

By choosing capacitors that are sufﬁciently large, you can reduce the ripple voltage to any desired level. This brute
force approach has disadvantages. A better approach to power-supply design is to use enough capacitance to reduce
ripple to low levels (perhaps 10% of the dc voltage), then use an active feedback circuit
to eliminate the remaining ripple.

## Circuit applications of diodes



