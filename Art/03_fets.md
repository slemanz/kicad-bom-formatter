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

You can usually ﬁnd a way to convert a circuit that uses BJTs into one using
FETs - but the new circuit may not be an improvement!

- High-impedance/low-current: Buffers or ampliﬁers for applications in which the base current and ﬁnite input
impedance of BJTs limit performance. Current practice favors using integrated circuits built with FETs.
Some of these use FETs as a high-impedance frontend for an otherwise bipolar design, whereas others use
FETs throughout.

- Analog switches: MOSFETs are excellent voltage-controlled analog switches, you
should generally use dedicated “analog switch” ICs, rather than building discrete circuits.

- Digital logic: MOSFETs dominate microprocessors, memory, special-purpose VLSI, and most high-performance
digital logic.

- Power switching: Power MOSFETs are usually preferable to ordinary bipolar power transistors for switching
loads.

- Variable resistors; current sources: In the “linear” region of the drain curves, FETs behave like voltage-controlled
resistors; in the “saturation” region they are voltage-controlled current sources.

- Generalized replacement for bipolar transistors: You can use FETs in oscillators, ampliﬁers, voltage regula-
tors, and radiofrequency circuits (to name a few), where bipolar transistors are also normally used. FETs aren’t
guaranteed to make a better circuit - sometimes they will, sometimes they won’t. You should keep them in
mind as an alternative.

## FET linear circuits

JFETs, which are well suited to linear applications such as current sources, followers,
and ampliﬁers. If you need a low-noise ampliﬁer with extremely high input impedance, the JFET is your friend (and
maybe your only friend).

Many JFETs come in families of three or four parts, graded by I_DSS and V_GS(off) , which alleviates somewhat
the annoying circuit design problems created by the wide spread of those parameters.

- JFET current sources: used as current sources within integrated circuits (particularly op-amps), and also sometimes
in discrete designs. We chose a JFET, rather than a MOSFET, because it needs no gate bias.

- FET ampliﬁers: source followers and common-source FET ampliﬁers are analogous to the emitter followers and common-emitter
ampliﬁers made with bipolar transistors that we talked about in the previous chapter. However, the absence of
dc gate current makes it possible to realize very high input impedances. Such ampliﬁers are essential when dealing
with the high-impedance signal sources encountered in measurement and instrumentation. For some specialized
applications you may want to build followers or ampliﬁers with discrete FETs; most of the time, however, you can take
advantage of FET-input op-amps. In either case it’s worth knowing how they work.

- Differential ampliﬁers: 