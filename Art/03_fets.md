# 3. FETs

Field-effect transistors (FETs) are different from the bipolar transistors, however, they are
similar devices, which we might call charge-control devices: in both cases we have a three-terminal
device in which the conduction between two electrodes depends on the availability of charge carriers,
which is controlled by a voltage applied to a third control electrode.

Here’s how they differ: in a bipolar transistor the collector–base junction is back-biased, so no current
normally ﬂows. Forward-biasing the base–emitter junction, overcomes its diode “contact potential barrier,
causing electrons to enter the base region, where they are strongly attracted to the collector.
This results in a collector current, controlled by a (much smaller) base current.

In an FET, as the name suggests, conduction in a channel is controlled by an electric ﬁeld, produced by a
voltage applied to the gate electrode. There are no forward-biased junctions, so the gate draws no current.

The FET’s nonexistent gate current is its most important characteristic. The resulting high input impedance
(which can be greater than 10 ohms) is essential in many applications, and in any case it makes circuit design
simple and fun. For applications like analog switches and ampliﬁers of ultra-high input impedance, FETs have
no equal. They can be easily used by themselves or combined with bipolar transistors to make integrated circuits.

There are a variety of FET types. Of the eight resulting possibilities, six could be made, and ﬁve actually
are. Four of those ﬁve are of major importance.

At the n-channel enhancement-mode MOSFET, which is analogous to the npn bipolar transistor. In normal operation
the drain (∼collector) is more positive than the source (∼emitter). No current ﬂows from drain to source unless
the gate (∼base) is brought positive with respect to the source.

## FET types

- n-channel, p-channel: FETs (like BJTs) can be fabricated in both polarities. Thus the mirror twin of our
n-channel MOSFET is a p-channel MOSFET. Its behavior is symmetrical.

- MOSFET, JFET:  MOSFET uses an insulated gate controlled by voltage to create an electric field, while a JFET
uses a PN junction to create a depletion region that controls the current.

- Enhancement, depletion: The n-channel MOSFETs were nonconducting, with zero gate bias, and were driven into
conduction by bringing the gate positive with respect to the source. This kind of FET is known
as enhancement mode. The other possibility is to manufacture the n-channel FET with the channel semiconductor
“doped” so that there is plenty of channel conduction even with zero gate bias, and the gate must be reverse-biased
by a few volts to cut off the drain current. Such a FET is known as depletion mode.

## Basic FET circuits