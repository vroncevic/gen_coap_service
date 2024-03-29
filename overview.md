# CoAP

CoAP is the Constrained Application Protocol from the CoRE (Constrained
Resource Environments) IETF group.

### Architecture

Like HTTP, CoAP is a document transfer protocol. Unlike HTTP, CoAP is designed
for the needs of constrained devices.

CoAP packets (4 bytes minimum) are much smaller than HTTP TCP flows.
Bitfields and mappings from strings to integers are used extensively to
save space. Packets are simple to generate and can be parsed in place
without consuming extra RAM in constrained devices.

Based on message model, four message types are Defines, and the message is
the data communication carrier, and the data communication between devices
is realized by exchanging network messages.

CoAP runs over UDP, not TCP. Clients and servers communicate through
connectionless datagrams. Retries and reordering are implemented in the
application stack. Removing the need for TCP may allow full IP networking
in small microcontrollers. CoAP allows UDP broadcast and multicast to be
used for addressing (which can send requests to multiple devices at the
same time (such as CoAP client search for CoAP Server)).

CoAP follows a client/server model. Clients make requests to servers, servers
send back responses (both parties can be in the client or server role).
Clients may GET, PUT, POST and DELETE resources. The request and response
packets are placed in the CoAP message for transmission.

CoAP is designed to interoperate with HTTP and the RESTful web at large
through simple proxies.

Because CoAP is datagram based, it may be used on top of SMS and other packet
based communications protocols.

The interaction model of CoAP is similar to the client/server model of HTTP.
However, machine-to-machine interactions typically result in a CoAP
implementation acting in both client and server roles. A CoAP request is
equivalent to that of HTTP and is sent by a client to request an action
(using a Method Code) on a resource (identified by a URI) on a server.
The server then sends a response with a Response Code; this response may
include a resource representation.

Unlike HTTP, CoAP deals with these interchanges asynchronously over a
datagram-oriented transport such as UDP. This is done logically using a layer
of messages that supports optional reliability (with exponential back-off).
CoAP Definess four types of messages: Confirmable, Non-confirmable,
Acknowledgement, Reset. Method Codes and Response Codes included in some of
these messages make them carry requests or responses. The basic exchanges of
the four types of messages are somewhat orthogonal to the request/response
interactions; requests can be carried in Confirmable and Non-confirmable
messages, and responses can be carried in these as well as piggybacked in
Acknowledgement messages.

One could think of CoAP logically as using a two-layer approach, a CoAP
messaging layer used to deal with UDP and the asynchronous nature of the
interactions, and the request/response interactions using Method and Response
Codes. CoAP is however a single protocol, with messaging and request/response
as just features of the CoAP header.

![Abstract layering of CoAP](https://raw.githubusercontent.com/vroncevic/gen_coap_service/dev/docs/abstract_layering_of_coap.png)

### Application Level QoS

Requests and response messages may be marked as “confirmable” or
“nonconfirmable”. Confirmable messages must be acknowledged by the receiver
with an ack packet.

Nonconfirmable messages are “fire and forget”.

### Content Negotiation

Like HTTP, CoAP supports content negotiation. Clients use Accept options to
express a preferred representation of a resource and servers reply with a
Content-Type option to tell clients what they’re getting. As with HTTP, this
allows client and server to evolve independently, adding new representations
without affecting each other.

CoAP requests may use query strings in the form ?a=b&c=d . These can be used
to provide search, paging and other features to clients.

### Security

Because CoAP is built on top of UDP not TCP, SSL/TLS are not available to
provide security. DTLS, Datagram Transport Layer Security provides the same
assurances as TLS but for transfers of data over UDP. Typically, DTLS capable
CoAP devices will support RSA and AES or ECC and AES.

### Observe

CoAP extends the HTTP request model with the ability to observe a resource.
When the observe flag is set on a CoAP GET request, the server may continue
to reply after the initial document has been transferred. This allows servers
to stream state changes to clients as they occur. Either end may cancel the
observation.

### Resource Discovery

CoAP Definess a standard mechanism for resource discovery. Servers provide a
list of their resources (along with metadata about them) at /.well-known/core.
These links are in the application/link-format media type and allow a client
to discover what resources are provided and what media types they are.

### NAT Issues

In CoAP, a sensor node is typically a server, not a client (though it may be
both). The sensor (or actuator) provides resources which can be accessed by
clients to read or alter the state of the sensor.

As CoAP sensors are servers, they must be able to receive inbound packets.
To function properly behind NAT, a device may first send a request out to
the server, as is done in LWM2M, allowing the router to associate the two.
Although CoAP does not require IPv6, it is easiest used in IP environments
where devices are directly routable.

### Comparison MQTT vs CoAP

MQTT and CoAP are both useful as IoT protocols, but have fundamental differences.

MQTT is a many-to-many communication protocol for passing messages between
multiple clients through a central broker. It decouples producer and consumer
by letting clients publish and having the broker decide where to route and
copy messages. While MQTT has some support for persistence, it does best as a
communications bus for live data.

CoAP is, primarily, a one-to-one protocol for transferring state information
between client and server. While it has support for observing resources, CoAP
is best suited to a state transfer model, not purely event based.

MQTT clients make a long-lived outgoing TCP connection to a broker. This usually
presents no problem for devices behind NAT. CoAP clients and servers both send
and receive UDP packets. In NAT environments, tunnelling or port forwarding
can be used to allow CoAP, or devices may first initiate a connection to the
head-end as in LWM2M.

MQTT provides no support for labelling messages with types or other metadata
to help clients understand it. MQTT messages can be used for any purpose, but
all clients must know the message formats up-front to allow communication.
CoAP, conversely, provides inbuilt support for content negotiation and discovery
allowing devices to probe each other to find ways of exchanging data.

Both protocols have pros and cons, choosing the right one depends on your application.

[Specification](https://datatracker.ietf.org/doc/html/draft-ietf-core-coap)
