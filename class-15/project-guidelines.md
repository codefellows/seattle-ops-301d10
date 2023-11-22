# Ops 301 Final Project Guidelines

## Scenario & Problem Domain

You team is tasked with updating the core IT infrastructure of a recent client company acquisition. This young, innovative startup aligns well with the mission of the client company; unfortunately, its IT systems do not.

Your team believes that trying to integrate the acquisition's existing intranet directly into the rest of the client company will result in technical debt. Since the acquisition is still a small startup, your team believes it will be better to simply build out a new infrastructure which is in line with the rest of the client company's holdings.

However, you still need to convince your leadership by demonstrating that your team is up to the challenge and can perform this kind of task in a repeatable, efficient manner.

Your team's task is to create a plan to make this acquistion successful and meet your client company's needs, then present your solutions to the client company on presentation day.

The operations chosen for this demonstration are:
- Develop a repeatable means of standing up a DC to oversee the new acquisition's network. The AD will need to automatically populate users and OUs in accordance with the organizational chart.
  - Objective: as a team, develop a Powershell script to be executed on a new installation of Windows Server.
    - This should be written as a single script, though it can be organized into different files.
    - The VM will need to reboot at least once while the script is performing its tasks.
      - Ways that students got their script to continue after reboot:
        - programmed the next bit of the script to the Windows startup folder (this is probably the cleverest)
    - How will you make sure the script completes its operations? Is there a way to avoid manually restarting/continuing the script after a reboot?
    - Each individual of the team is to contribute their share of the overall script and document their individual contribution. The final script should reflect an equal effort from all team members.
    - Minimum operations this script should perform:
      - Fully standup all requisite services to make the server into a DC
      - Assign the Windows Server VM a static IPv4 address and a DNS
        > Note: in class we assigned a *reserved IP* in pfSense, but this script is to assign the VM a *static IP*.
      - Rename the Windows Server VM
      - Installs AD-Domain-Services
      - Create an AD Forest, Organizational Units (OU), and users
- Develop a secure solution for data transmission between two networks, and demonstrate successful resource access in your upcoming presentation to the executive team.
  - Objective:
    - Build a site-to-site VPN tunnel
    - Alter at least one parameter compared to what was performed in class (e.g. router used, VPN protocol used, introducing a cloud component, etc.)
    - Demonstrate successful access to a file server, Active Directory, or other network resource on the other end of the tunnel
- The client company's leadership has concerns about the local network security of the new company, if the acquisition's intranet to going to be joined to the client company. You will need to demonstrate implementation of some form of network access control that provides a healthy level of AAA security management.
  - Objective: Deploy a RADIUS system that raises a captive portal for new network users and authenticates them using AD credentials.
- What other possible vulnerabilities is your team concerned about? Does your team have any additional suggestions or solutions to any oversight?

## Stretch Goal

Your client company has been wanting to move their physical infrastructure to the cloud and this is the perfect opportunity to build it out in AWS! If you team has time, reach for this stretch goal by meeting the following requirements:

- Decide which departments in your org chart need public or private subnets.
  - Create a description of the department and why it needs to be private or public.
  - Document your reasoning for each design choice either in a Google Doc linked in a repo or in a markdown file.
- Draw out your team's proposed AWS VPC topology solution
  - Don't forget to include IP addresses!
- Build out your team's AWS VPC solution in the cloud!
  - Make the necessary connections and configurations to meet your client company's needs, including the newly acquired company.
- Hint: In an AWS environment, you could deploy a Windows Server instance within a VPC and use Active Directory as the user management system for those instances.

> Tip: You can use AI tooling to help you generate storylines to validate your infrastructure design choices.

## Client Company and Org Chart

Use your favorite AI tool to generate a fictional client company, acquired company and org chart. This is your opportunity to be creative!

Try AI prompts like:
- "Build me a fictional org chart, including an executive team and at least 4 different roles in each department, using disney movie characters."
- "Can you add an additional smaller company that is being acquired by the above org chart?
- "Can you give me a short description about the acquired company?"
- "How do I structure an AWS VPC to fit this org chart?"
- "Which subnets should be public and private?"

## Assignments & Deliverables

- Keep an eye on Canvas for assignments due this week.
- Remember to complete nightly Project Report assignments. These assignments are easy to forget as you get swept up in interesting project subject matter.
- Necessities such as the Team Agreement (conflict resolution, etc.) and the Project Plan will be created in your Project Prep assignments. Instructor approval is required before progressing to the next Project Prep assignment.
- You will need to submit a preliminary link to your deliverables for instructor review a few days before presentations.
- You will need to give give a practice presentation to your instructor. Make this as close as possible to how you plan to present -- try not to break character, give assides or explanations, or engage in crosstalk.
- By demo day, you'll need these deliverables assembled:
  - Demo day slide deck
  - Project Reports
  - Project Prep Assignments
  - Link to GitHub Org
  - Google drive docs (linked in repo)
- Track your individual contributions throughout the project so that you can easily submit your individual contributions writeup on demo day for grading.

## Standup

Every day, the instructional team will circulate to your group for a formal "Standup Meeting". Standup should take approximately 10 minutes per team.

> Standups give the instructional team insight into the current status of your project and the progress the team hopes to make each day.

During standup, each team member will address these three points:

  1. What you individually accomplished yesterday
  1. What you individually plan to accomplish today
  1. Anything that is blocking you from making progress

## Presentation Prep

Your team will practice your presentation prior to the final presentation day. This is typically scheduled by the instructional team. During the practice presentation, the instructional team will provide constructive feedback about the flow of the presentation and delivery of the subject matter.

Practice and prepare your technical demonstrations in advance of demo day to rule out any quirks/bugs.

General slide deck guidelines:
- The presentation slides must use the aesthetic formatting of the [template slide deck](https://docs.google.com/presentation/d/1NeXKKEpjK2DDme8EwlZBsJndUqIgGYzWrY6FAYtNTf0/edit).
  - Remember to create your own copy of the template and do not edit the template itself.
- Ensure your timing is no more than 20 minutes long, including some time at the end for questions.
- Present from the slide deck and demo on your shared screen.
- Each member should introduce themselves with their personal pitch.

Each member of the team must have a speaking part. It is okay to use presenter notes/outlines but remember to avoid reading notes verbatim and to present naturally as if speaking to a friend.

The appropriate dress code is business casual - not too formal and not too casual.

Be cognizant of the environment you're presenting from. A clean backdrop, good lighting, and quality mic and webcam go a long ways.

In addition to the scheduled practice session, the team is encouraged to continue to practice on their own. Keep track of the time and adjust accordingly. Practice transitioning speaking segments.

Speak clearly and do not use slang or profanity. Take it seriously and be professional.

## Grading

Each team member's grade is split between their individual effort, and the project's technical merit.

Individual effort is graded based on contributions to project deliverables, and professionalism in the presentation.

Technical merit of the project overall is evaluated according the requirements. The Project Grade is a combination of the Presentation (55%) and the Deliverables (45%)

### Presentation (55%)

Components of the presentation must include:

- A. Team members individually introduce themselves. (5 min)
  - A1. One interesting/fun fact about yourself
  - A2. Your career ambitions (where you've been, where you're going, and why)
- B. Topical Overview (5 min)
  - B1. As the "Problem Domain", describe the project scenario you were assigned and the overall client requirements.
  - B2. What solutions to the problem domain will your team be presenting today? Why did you choose these solutions?
  - B3. Before & After Network topology diagram of the subsidiary's network(s).
    - What kind of network is this?
    - Design philosophy
    - Remote access considerations
- C. Improvements made to network infrastructure to accommodate remote employees and site-to-site connectivity (5 min)
  - C1. Implementation of virtual private networking (VPN) and demonstrate successful resource access
  - C2. Network access controls system
    - How does your system achieve AAA network security management principles?
- D. Powershell scripts that automates DC deployment (5 min)
  - D1. Present the scenario org chart
  - D2. Script should demonstrably perform:
    - Assigns the Windows Server VM a static IPv4 address
    - Assigns the Windows Server VM a DNS
    - Renames the Windows Server VM
    - Installs AD-Domain-Services
    - Creates an AD Forest
    - Creates Organizational Units (OU)
    - Creates users
- E. Final thoughts on how the project went (5 min)
  - E1. The team's approach to planning and communication throughout the project
  - E2. A technical obstacle or two and how those obstacles were overcome
  - E3. A portion of the outcome that each team member is particularly proud of
- F. Q&A (5 min)

### Deliverables (45%)

Submit to instructor a single link to your Github Org. All team members are to contribute an equal share to documentation corresponding to the components they worked on and should clearly indicate which components each contributed to in their individual project submission notes.

- GitHub Repository (10%)
  - A repo under an appropriately name Github "Organization"
  - Sufficient documentation in the top level README to explain to a stranger who you are, what this project was about, and how all of the material in the repo pertains to it.
    - This README should be:
      - Attractively formatted
      - Include links to relevant files in the repo
      - Include links to each of your own Github accounts AND LinkedIn accounts
  - All other deliverables should be included as files in this repo
- Presentation Material (5%)
  - Slide deck, as a PDF, link in the repo
  - A link to the video of your presentation (when it becomes available) in the repo
- Network design (20%)
  - A network topology diagram of your systems architecture design.
    - All components must be labeled, and network diagram must be presentable (straight lines) and free of defects/typographical issues. Take your time to create a quality network diagram; do not rush!
    - Clearly indicate what devices are hosting network services, like DHCP, DNS, etc.
  - A clear, written explaination and justification your network design.
    - Include a table or chart of network infrustructure and configuration details (yes, this will overlap with your topology -- you must document your network in both ways):
      - Subnets and their uses
        - Include Subnet Masks, CIDR addresses, etc.
      - DHCP ranges
        - Lease pools
        - Ranges of addresses reserved for particular uses
      - Firewall rules
      - Roles and IP address of all important devices (everything but endpoints)
- SOP and Policy Documentation (10%)
  - SOP Requirements:
    - Each SOP should include the following sections:
      - Purpose
      - Scope
      - Responsibilities
      - Prerequisites
      - Procedures
      - References
      - Definitions
      - Revision History (including who contributed to each revision)
    - For **each** SOP included in your MSP SOW deliverable, attribute authorship to the team member
    - SOPs can either be:
      - Worked on as google docs and submitted as PDFs linked in the repo
      - Worked on and submitted as Markdown files in the repo
    - SOPs should share a common format (see [SOP-example-template](./SOP-example-template.md))
    - SOPs should be submitted either as individual documents or as a single document (either PDF or Markdown) with a linked table of contents

    - Compose thorough SOPs for each of the following:
      - How will network account needs be handled for employees being onboarded?
      - How will network account needs be handled for employees being terminated?
      - How will OS version control be handled?
        - Hint: Read [Windows Server Update Services](https://docs.microsoft.com/en-us/windows-server/administration/windows-server-update-services/get-started/windows-server-update-services-wsus){:target="_blank"}.
      - How will you ensure users can access their files from any domain attached system?
      - How will you monitor network traffic?
      - How will you manage change to the network (such as hardware, software, or configuration changes) while minimizing network disruptions and downtime?
      - How will you manage and maintain network security?

Teams are encouraged to ask their instructional team for feedback on project report, slide deck, and other deliverables. The client point of contact should be contacted via email regarding scenario-specific scoping.
