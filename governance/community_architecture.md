(community_architecture)=
# Community Architecture

:::{tikz} caption

\tikzset{%
  block/.style    = {draw, thick, rectangle, minimum height = 3em,
    minimum width = 3em},
  sum/.style      = {draw, circle, node distance = 2cm}, % Adder
  input/.style    = {coordinate}, % Input
  output/.style   = {coordinate} % Output
}

\draw
	% Drawing the blocks of first filter :
	node at (0,0)[right=-3mm]{\Large \textopenbullet}
	node [input, name=input1] {}
	node [sum, right of=input1] (suma1) {$+$}
	node [block, right of=suma1] (inte1) {$\int$}
         node at (6.8,0)[block] (Q1) {\Large $Q_1$}
         node [block, below of=inte1] (ret1) {\Large$T_1$};
    % Joining blocks.
    % Commands \draw with options like [->] must be written individually
	\draw[->](input1) -- node {$X(Z)$}(suma1);
 	\draw[->](suma1) -- node {} (inte1);
	\draw[->](inte1) -- node {} (Q1);
	\draw[->](ret1) -| node[near end]{} (suma1);
	% Adder
\draw
	node at (5.4,-4) [sum, name=suma2] {$+$}
    	% Second stage of filter
	node at  (1,-6) [sum, name=suma3] {$+$}
	node [block, right of=suma3] (inte2) {$\int$}
	node [sum, right of=inte2] (suma4) {$+$}
	node [block, right of=suma4] (inte3) {$\int$}
	node [block, right of=inte3] (Q2) {\Large$Q_2$}
	node at (9,-8) [block, name=ret2] {\Large$T_2$}
;
	% Joining the blocks of second filter
	\draw[->] (suma3) -- node {} (inte2);
	\draw[->] (inte2) -- node {} (suma4);
	\draw[->] (suma4) -- node {} (inte3);
	\draw[->] (inte3) -- node {} (Q2);
	\draw[->] (ret2) -| (suma3);
	\draw[->] (ret2) -| (suma4);
         % Third stage of filter:
	% Defining nodes:
\draw
	node at (11.5, 0) [sum, name=suma5]{$+$}
	node [output, right of=suma5]{}
	node [block, below of=suma5] (deriv1){$\frac{d}{dt}$}
	node [output, right of=suma5] (sal2){}
;
	% Joining the blocks:
	\draw[->] (suma2) -| node {}(suma3);
	\draw[->] (Q1) -- (8,0) |- node {}(ret1);
	\draw[->] (8,0) |- (suma2);
	\draw[->] (5.4,0) -- (suma2);
	\draw[->] (Q1) -- node {}(suma5);
	\draw[->] (deriv1) -- node {}(suma5);
	\draw[->] (Q2) -| node {}(deriv1);
    	\draw[<->] (ret2) -| node {}(deriv1);
    	\draw[->] (suma5) -- node {$Y(Z)$}(sal2);
    	% Drawing nodes with \textbullet
\draw
	node at (8,0) {\textbullet}
	node at (8,-2){\textbullet}
	node at (5.4,0){\textbullet}
    	node at (5,-8){\textbullet}
    	node at (11.5,-6){\textbullet}
    	;
	% Boxing and labelling noise shapers
	\draw [color=gray,thick](0,0) rectangle (14,14);
	\draw [color=gray,thick](2,0) rectangle (12,11);
	\draw [color=gray,thick](4,0) rectangle (10,8);
	\node at (-0.5,1) [above=5mm, right=0mm] {\textsc{first-order noise shaper}};
	\draw [color=gray,thick](-0.5,-9) rectangle (12.5,-5);
	\node at (-0.5,-9) [below=5mm, right=0mm] {\textsc{second-order noise shaper}};
:::

:::{graphviz}
:name: community-diagram
:align: center

digraph "community-architecture" {
    rankdir="RL";
    compound=true;

    irr_contrib [label="Irregular contributors"];
    db_contrib [label="Drive-by contributors"];

    interns [label = "GSoC interns"];
    contractors [label = "Independent Contractors"];
    employed_recurr [label = "Employed"];
    volunteer_recurr [label = "Volunteer"];

  subgraph cluster_contrib {
    style=rounded;
    label = "Contributors";
    labelloc = "b";

    irr_contrib;
    db_contrib;

    employed_core [label = "Employed"];
    volunteer_core [label = "Volunteer"];

    subgraph cluster_recurr {
      label = "Recurring Contributors";
      href = "https://www.arviz.org/en/latest/our_team.html#recurrent-contributors";

      interns;
      contractors;
      employed_recurr;
      volunteer_recurr;

      subgraph cluster_paid1 {label="Paid"; interns; contractors; employed_recurr; }

      subgraph cluster_core {
        label = "Core Contributors";
        href = "https://www.arviz.org/en/latest/our_team.html#core-contributors";

        node_core [shape=point];
        employed_core;
        volunteer_core;

        subgraph cluster_paid2 {label="Paid"; employed_core; }

        subgraph cluster_council {
          label = "Random Variables Council";

          node_council [style=invis, shape=point]; // bogus node
        }
      }
    }
  }

  numfocus [label = "NumFOCUS", href = "https://numfocus.org"];
  inst_partners [label = "Institutional Partners",
    href="https://www.arviz.org/en/latest/sponsors_partners.html#institutional-partners"];
  sponsors [label = "Sponsors",
    href="https://www.arviz.org/en/latest/sponsors_partners.html#sponsors"];

  node_council -> numfocus [dir = both, ltail=cluster_council];
  sponsors -> node_core [dir = both, lhead=cluster_core];
  inst_partners -> employed_recurr;
  inst_partners -> employed_core;
  node_core -> employed_core [lhead=cluster_paid2];
  node_core -> employed_recurr [lhead=cluster_paid1];
}
:::

* General Contributors
* {ref}`recurrent_contributor_description`
* {ref}`core_contributor_description` (of which Council members are also a part of)
* 7 Person steering council ({ref}`council_description`)

Anyone working with ArviZ has the responsibility to personally uphold
the Code of Conduct. Core Contributors have the additional responsibility
of _enforcing_ the Code of Conduct to maintain a safe community.

(recurrent_contributor_description)=
## Recurrent Contributors
Recurrent Contributors are those individuals who contribute recurrently to the
project and can provide valuable insight on the project.
They are therefore actively consulted and can participate in the same communication
channels as Core Contributors. However, unlike Core Contributors,
Recurrent Contributors don't have voting, managing or writing rights.

In practice, this translates in participating from private team discussions
(i.e. in Slack or live meetings) but not being able to vote in elections
for the Random Variables Council members nor having commit rights on GitHub.

The Recurrent Contributor position will often be an intermediate step for people
in becoming Core Contributors once their contributions are frequent enough
and during a sustained period of time.
But it is also an important role by itself for people who want to be part of
the project on a more advisory-like role, as they for example might not have
the time availability or don't want the responsibilities that come
with being a Core Contributor.

The process for new people to join the project as recurrent contributors is
described at {ref}`contributor_onboarding`. Recurrent or core contributors
can nominate anyone to join the project as a recurrent contributor.

### Current Recurrent Contributors
Current recurrent contributors are listed {ref}`on this page <recurrent_contributor_list>`

(core_contributor_description)=
## Core Contributors
Core Contributors are those who have provided consistent and meaningful contributions to ArviZ.
These can be, but are not limited to, code contributions, community contributions, tutorial
development etc. Core Contributors will be given the ability to manage the ArviZ GitHub
repository, including code merges to main. This does not necessarily mean Core Contributors
must submit code, but more so signifies trust with the project as a whole.

The process for new people to join the project as core contributors is
described at {ref}`contributor_onboarding`. Only recurrent contributors
are eligible to become core contributors, and only core contributors
can nominate them.

### Core Contributor Responsibilities
* Enforce code of conduct
* Maintain a check against Council

### Current Core Contributors
Current core contributors are listed {ref}`on this page <core_contributor_list>`

(council_description)=
## Random Variables Council
The Project will have a Steering Council that consists of Core Contributors
who have produced contributions that are substantial in quality and quantity,
and sustained over at least one year. The overall role of the Council is to
ensure, taking input from the Community, the
long-term well-being of the project, both technically and as a community.

During the everyday project activities, council members participate in all
discussions, code review and other project activities as peers with all other
Contributors and the Community. In these everyday activities, Council Members
do not have any special power or privilege through their membership on the
Council. However, it is expected that because of the quality and quantity of
their contributions and their expert knowledge of the Project Software and
Services that Council Members will provide useful guidance, both technical and
in terms of project direction, to potentially less experienced contributors.

### Council Responsibilities
Council Members will have the responsibility of
* Removing members, including Council Members, if they are in violation of the Code of Conduct
* Making decisions when regular community discussion does not produce consensus on an issue
  in a reasonable time frame. See {ref}`council_decision_process` page for more details.
* Making decisions about strategic collaborations with other organizations or individuals.
* Making decisions about the overall scope, vision and direction of the project.
* Developing funding sources
* Deciding how to disburse funds with consultation from Core Contributors

The council may choose to delegate these responsibilities to sub-committees. If so, Council members must update this document to make the delegation clear.

:::{important}
Individual council members do not have the power to unilaterally wield these
responsibilities. The council as a whole must jointly make these decisions.
In other words, Council Members are first and foremost Core Contributors, but only
when needed they can collectively make decisions for the health of the project.
:::

### Length of Tenure and Reverification
* Council members term limits are 4 years, after which point their seat will come up for reelection.
* Each year on April 7th council members will be asked to restate their commitment to being on the council
* Attempts should be made to reach every council member over at least 2 communication media. For example: email, Slack, phone, or GitHub.
* If a council member does not restate their commitment their seat will be vacated.
* Inactivity can be determined by lack of substantial contribution, including votes on council, code or discussion contributions, contributions in the community or otherwise.
* In the event of a vacancy in the council, an {ref}`election <council_selection>` will be held to fill the position.
* There is no limit on the number of terms a Council Member can serve

(current_rv_council)=
### Current Random Variables Council members
The current RV Council members are:

* Oriol Abril-Pla (@OriolAbril)
* Alex Andorra (@AlexAndorra)
* Seth Axen (@sethaxen)
* Colin Carroll (@ColCarroll)
* Ari Hartikainen (@ahartikainen)
* Ravin Kumar (@canyon289)
* Osvaldo Martin (@aloctavodia)
