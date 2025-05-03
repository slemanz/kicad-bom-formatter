# 2. BIPOLAR TRANSISTORS

The transistor is our most important example of an “active” component, a device that can amplify, producing an output
signal with more power in it than the input signal.

Devices with power gain are distinguishable by their ability to make oscillators, by feeding some output signal back
into the input.

The transistor is the essential ingredient of every electronic circuit, from the simplest ampliﬁer or oscillator to
the most elaborate digital computer. Integrated circuits (ICs), which have largely replaced circuits constructed
from discrete transistors, are themselves merely arrays of transistors and other components built from a single chip
of semiconductor material.

BJTs excel in accuracy and low noise, whereas FETs excel in low power, high impedance,
and high-current switching.

## First transistor model: current ampliﬁer

A bipolar transistor is a three-terminal device, in which a small current applied to the base
controls a much larger current ﬂowing between the collector and emitter.

## Some basic transistor circuits

**Transistor switch:** a small control current enables a much larger current to ﬂow in another circuit, is called
a transistor switch.

**Pulse generator:** By including a simple RC, you can make a circuit that gives a pulse output from a step input;
the time constant τ = RC determines the pulse width.

**Emitter follower:** It is called that because the output terminal is the emitter, which
follows the input (the base), less one diode drop:

**Emitter followers as voltage regulators:** The simplest regulated supply of voltage is simply a zener

**Emitter follower biasing:** When an emitter follower is driven from a preceding stage
in a circuit, it is usually OK to connect its base directly to the previous stage’s output.

**Current source:** Current sources, although often neglected, are as important and as useful as voltage sources.
They often provide an excellent way to bias transistors, and they are unequaled as “active loads” for super-gain
ampliﬁer stages and as emitter sources for differential ampliﬁers. Integrators, sawtooth generators, and ramp
generators need current sources.

**Unity-gain phase splitter:** Sometimes it is useful to generate a signal and its inverse, i.e., two signals 180°
out of phase. That’s easy to do – just use an emitter-degenerated ampliﬁer with a gain of −1.

**Transconductance:** the measure of how efficiently a transistor converts a small input voltage change into a
larger output current change. The voltage gain was then simply the ratio of collector (output) voltage swing to base
(input) voltage swing.

Before jumping into the complexity just ahead, let’s remind ourselves of the four transistor circuits we’ve seen, namely
the switch, emitter follower, current source, and common emitter ampliﬁer.

## Ebers–Moll model

The Ebers-Moll model is a simplified representation of a Bipolar Junction Transistor (BJT) that uses two diodes and two
current sources to model its behavior, particularly in DC biasing circuits.

We thought of the transistor as a current ampliﬁer whose input circuit behaved like a
diode. That’s roughly correct, and for some applications it’s good enough.

Although the Ebers–Moll equation tells us that the base–emitter voltage “programs” the collector current, this
property is not easy to use in practice (biasing a transistor by applying a base voltage) because of the large
temperature coefﬁcient of base–emitter voltage

### An aside: the perfect transistor

Looking at BJT transistor properties like the non-zero
(and temperature-dependent) VBE , the ﬁnite (and current-dependent) emitter impedance re and transconductance
gm , the collector current that varies with collector voltage (Early effect) etc., one is tempted to ask which transistor is
better? Is there a “best” transistor, or perhaps even a perfect transistor? If you search, you’ll see there is no
best transistor candidate.

That’s because all physical bipolar transistors are subject to the same device physics, and their parameters tend to scale
with die size and current, etc.

How does the perfect transistor work? A four-transistor circuit known as a diamond transistor
stage. This circuit is a variation of the cascaded pnp-npn emitter follower.

Texas Instruments calls their perfect transistor (its partnumber is OPA860 ) an Operational Transconductance
Ampliﬁer (OTA). Other names they use are “Voltage-Controlled Current source,” “Transconductor,” “Macro
Transistor".

### Current mirrors

The technique of matched base–emitter biasing can be used to make what is called a current mirror, an interesting
current-source circuit that simply reverses the sign of a “programming” current.

There are additional nice tricks you can do with current mirrors, such as generating multiple independent outputs,
or an output that is a ﬁxed multiple of the programming current.

### Differential amplifiers

The differential ampliﬁer is a very common conﬁguration used to amplify the difference voltage between two input
signals. In the ideal case the output is entirely independent of the individual signal levels – only the difference matters.

Some nomenclature: when both inputs change levels together, that’s a common-mode input change. A differential
change is called normal mode, or sometimes differential mode. A good differential ampliﬁer has a high common-
mode rejection ratio (CMRR), the ratio of response for a normal-mode signal to the response for a common-mode
signal of the same amplitude. CMRR is usually speciﬁed in decibels.

Because of its high gain and stable characteristics, the differential ampliﬁer is the main building block of the
comparator, , a circuit that tells which of two inputs is larger. They are used for all sorts
of applications: switching on lights and heaters, generating square waves from triangles, detecting when a level in
a circuit exceeds some particular threshold, class-D ampliﬁers and pulse-code modulation, switching power supplies,
etc. The basic idea is to connect a differential ampliﬁer so that it turns a transistor switch on or off, depending on the
relative levels of the input signals. The linear region of ampliﬁcation is ignored, with one or the other of the two
input transistors cut off at any time.

## Some ampliﬁer building blocks

**Push–pull output stages:** amplifier is a type of electronic circuit that uses a pair of active devices that alternately
supply current to, or absorb current from, a connected load. This kind of amplifier can enhance both the load capacity
and switching speed.

**Darlington connection:** A Darlington connection, also known as a Darlington pair or Darlington transistor, is a circuit
comprised of two bipolar junction transistors (BJTs) connected to achieve a high current gain and high input impedance. 
Behaves like a single transistor with beta equal to the product of the two transistor betas.

**Capacitance and Miller effect:** The Miller effect is a phenomenon in amplifier circuits where the apparent input
capacitance increases due to the amplifier's voltage gain. At high frequencies
the effects of capacitance often dominate circuit behavior; at 100 MHz a typical junction capacitance of 5 pF has an
impedance of just 320 ohms.

## Negative feedback

Feedback offers a cure to some vexing problems.
Feedback has become such a well-known concept that the word has entered the general vocabulary. In control systems,
feedback consists of comparing the actual output of the system with the desired output and making a correction
accordingly.

As used in ampliﬁers, negative feedback is implemented simply by coupling the output back in such a way as to
cancel some of the input.

A feedback network can be frequency dependent, to produce an equalization ampliﬁer (with speciﬁc gain-versus-frequency
characteristics), or it can be amplitude dependent, producing a nonlinear ampliﬁer. 

### Effects of feedback on ampliﬁer circuits

- Predictability of gain: The voltage gain is G = A/(1 + AB). In the limit of inﬁnite open-loop gain.

- Input impedance: Feedback can be arranged to subtract a voltage or a current from the input (these are sometimes called
series feedback and shunt feedback, respectively).

- Output impedance: feedback can extract a sample of the output voltage or the output current. In the ﬁrst case the open-loop output
impedance will be reduced by the factor 1 + AB, whereas in the second case it will be increased by the same factor.

- Sensing output current: feedback can be connected instead to sample the output current. It is possible to have multiple
feedback paths, sampling both voltage and current. In the general case the output impedance is given by Blackman’s
impedance relation.

## Some typical transistor circuits

Real-world circuits usually incorporate op-amps and other ICs.

- Regulated power supply: circuit, negative feedback acts to stabilize the output voltage

- Temperature controller: a temperature controller based on a thermistor sensing element, a
device that changes resistance with temperature.

- Simple logic with transistors and diodes: a circuit that performs a task,
sounding a buzzer if either car door is open and the driver is seated. In this circuit the transistors
all operate as switches.