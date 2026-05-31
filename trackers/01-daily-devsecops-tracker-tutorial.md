# Daily DevSecOps Tracker Tutorial

## 1. The Mental Model

File này không phải để "ghi cho đẹp". Nó là hệ điều hành cá nhân cho roadmap DevSecOps.

Nó trả lời:

* Hôm nay tôi làm gì?
* Việc đó map với concept nào?
* Tôi có evidence không?
* Tôi có đang quá tải không?
* Cuối tuần tôi có thứ gì đủ tốt để kể với senior/interviewer không?

Điểm quan trọng: tracker không thưởng cho số giờ cao. Nó thưởng cho việc có bằng chứng, có concept rõ, có kết luận, và có next action.

## 2. The 5-Minute Daily Routine

Mỗi ngày chỉ cần 5 phút:

1. Mở `Daily Log`.
2. Thêm một dòng cho task chính.
3. Chọn `Roadmap Phase`.
4. Chọn `Task Type`.
5. Ghi `Formal Concept`.
6. Ghi `Action Taken`.
7. Ghi `Evidence Produced?`.
8. Ghi `Time Spent`, `Energy`, `Sleep`, `School Risk`.
9. Ghi `Next Action`.
10. Nếu có evidence thật, thêm vào `Evidence Queue`.

Ví dụ một dòng tốt trong `Daily Log`:

| Field | Example |
| ----- | ------- |
| Date | 2026-05-27 |
| Roadmap Phase | Q1 Network and OS |
| Task Type | Measure |
| Category | Networking |
| System / Project | VyOS / Router |
| Formal Concept | Routing table lookup, default route |
| Hypothesis / Goal | Wrong gateway should select the wrong next hop. |
| Action Taken | Measured with `ip route`, `traceroute`, ARP table, and `tcpdump`. |
| Result | Confirmed next-hop mismatch and failed off-subnet path. |
| Evidence Produced? | Yes |
| Evidence Link / Path | `E:\Roadmaps\evidence\2026-05-27-route-measurement.md` |
| Time Spent Hours | 2.5 |
| Energy Level | 3 |
| Sleep Hours | 6.0 |
| School Risk Level | Yellow |
| Status | Done |
| Next Action | Fix config and compare before/after output. |

## 3. How to Fill Daily Log

### Identity columns

`Date`, `Day`, `Week Number`, `Month`, `Quarter`.

Bạn nhập `Date`. Workbook đang có công thức để tự tính `Day`, `Week Number`, `Month`, `Quarter`. Đừng ghi tay vào các cột công thức trừ khi bạn biết rõ đang làm gì.

### Roadmap columns

`Roadmap Phase`, `Task Type`, `Category`, `System / Project`.

Chọn đúng phase để tránh học lệch:

* Q1: Network and OS.
* Q2: Kubernetes and Runtime.
* Q3: Database and Security.
* Q4: Production and Portfolio.
* School-heavy mode: khi việc trường/GPA cần ưu tiên.
* Recovery: khi mục tiêu đúng là phục hồi, không phải ép thêm lab.

### Engineering columns

`Formal Concept`, `Hypothesis / Goal`, `Action Taken`, `Result`.

Đây là phần biến homelab thành engineering learning.

Xấu:

* "fix network"
* "study kubernetes"
* "debug bug"

Tốt:

* "Measured failed default route using `ip route`, `traceroute`, `tcpdump`; confirmed next-hop mismatch."
* "Mapped VLAN trunking to IEEE 802.1Q tagging and identified where L2 ends and L3 routing starts."
* "Compared readiness probe failure with running process; confirmed service removed pod from endpoints."

### Evidence columns

`Evidence Produced?`, `Evidence Link / Path`, `Break?`, `Measure?`, `Fix?`, `Document?`.

`Evidence Produced?` không phải cảm giác. Nếu chọn `Yes`, phải có path/link đủ rõ. Nếu chỉ có raw note hoặc screenshot chưa dọn, chọn `Partial` cũng được, nhưng nên thêm vào Evidence Queue.

`Break?`, `Measure?`, `Fix?`, `Document?` giúp bạn nhìn xem task đang ở đoạn nào của vòng `Break -> Measure -> Fix -> Document`.

### Health and risk columns

`Time Spent Hours`, `Energy Level`, `Sleep Hours`, `School Risk Level`, `Chaos Mode?`.

Nhập trung thực. Nếu ngủ dưới 6h, đừng tự ép failure injection. Nếu School Risk Yellow/Red, giảm scope. Nếu Chaos Mode Yes, không mở lab mới chỉ vì thấy "còn thiếu tiến độ".

### Closure columns

`Status`, `Notes`, `Next Action`.

`Next Action` phải đủ cụ thể để ngày mai mở file lên là biết làm gì. Ví dụ: "Add tcpdump evidence for VLAN path" tốt hơn "continue".

## 4. How to Use Dashboard

Mở `Dashboard` để xem tuần hiện tại:

* `Total Focus Hours`: tổng giờ focus trong Daily Log.
* `Evidence Items Created`: số dòng Daily Log có evidence `Yes` hoặc `Partial`.
* `Average Sleep Hours`: ngủ trung bình theo Daily Log.
* `School Risk`: có Red/Yellow trong tuần không.
* `WIP Status`: trạng thái WIP mới nhất.
* `Chaos Mode Days`: số ngày Chaos Mode On.
* `Alerts`: cảnh báo như sleep debt, work without evidence, school risk red, WIP violation.

Không dùng dashboard để tự lừa mình. Nếu Total Focus Hours cao nhưng Evidence Items thấp, đó không phải "tuần năng suất"; đó là tuần cần sửa cách làm.

Một câu hỏi nên tự hỏi khi xem Dashboard:

> Tuần này số giờ có biến thành evidence, review, document, hoặc decision không?

## 5. How to Use Evidence Queue

Evidence không cần hoàn hảo ngay. Level 0 raw vẫn có giá trị, vì raw evidence giúp bạn không mất dấu sự thật.

Nhưng evidence phải nâng dần:

* Level 0: raw log/screenshot/command.
* Level 1: cleaned observation.
* Level 2: lab report.
* Level 3: postmortem/ADR.
* Level 4: portfolio case study.

Thêm dòng vào `Evidence Queue` khi có:

* command/log/screenshot quan trọng;
* packet capture;
* metric graph;
* config diff;
* postmortem;
* diagram;
* lab report.

Đừng chỉ ghi "có screenshot". Ghi rõ:

* nó nằm ở đâu;
* nó chứng minh gì;
* nó không chứng minh gì;
* có cần cleanup không;
* có phải portfolio candidate không.

Ví dụ:

| Field | Example |
| ----- | ------- |
| Evidence Type | Packet Capture |
| Evidence Level | Level 1 Clean Observation |
| What It Proves | Wrong gateway sends traffic to unexpected next hop. |
| What It Does Not Prove | It does not prove app-level availability. |
| Needs Cleanup? | No |
| Portfolio Candidate? | No |

## 6. How to Use Weekly Review

Chủ nhật mở `Weekly Review` và trả lời 5 câu:

* What did I break?
* What did I measure?
* What theory did I map it to?
* What evidence did I produce?
* What would a senior engineer reject as hand-wavy?

Câu 5 là quan trọng nhất. Nếu bạn không biết senior sẽ reject chỗ nào, khả năng cao bạn đang viết review để tự an ủi, không phải để nâng chất lượng.

Ví dụ trả lời tốt:

* What did I break? `A test VM default gateway was changed to an invalid gateway.`
* What did I measure? `ip route, traceroute, ARP table, tcpdump on the relevant interface.`
* What theory did I map it to? `Routing table lookup, default route behavior, L3 forwarding.`
* What evidence did I produce? `Command transcript and lab report path.`
* What would be rejected? `Topology diagram still lacks subnet labels and gateway interface names.`

Nếu review status là `Needs Fix`, tuần sau nên ưu tiên fix evidence/document trước khi mở lab mới.

## 7. How to Use WIP Limit

Luật WIP:

* 1 university deliverable.
* 1 certification track.
* 1 homelab experiment/document.

OK:

* University: report chapter.
* Certification: CCNA subnetting.
* Homelab: `network-ground-truth.md`.

Violation:

* vừa Kubernetes;
* vừa ZAP;
* vừa NetBox;
* vừa CCNA;
* vừa bài trường.

Khi `WIP Limit Status = Warning`, giảm scope. Khi `Violation`, phải pause/drop việc optional. Đừng mở thêm "chỉ một chút thôi"; đó là cách tracker mất tác dụng.

## 8. How to Use Chaos Mode

Chaos Mode không phải thất bại. Nó là cơ chế bảo vệ.

Bật Chaos Mode khi:

* 2 deadline trong 7 ngày;
* exam trong 5 ngày;
* ngủ dưới 6h trong 2 đêm;
* lab unresolved sau 2h;
* group assignment phụ thuộc vào bạn;
* context switching quá chậm.

Khi Chaos Mode On, allowed:

* school deadline;
* keep services stable;
* theory mapping note;
* evidence parking;
* documentation only;
* maintenance review;
* recovery.

Banned:

* new failure injection;
* new infrastructure change;
* new Kubernetes topic;
* aggressive scan;
* late-night debugging;
* optional tool setup.

Nếu On mà `Banned Work` trống, hãy điền ngay. Khi đầu óc mệt, quyết định cấm trước giúp bạn không tự phá scope.

## 9. How to Use School Risk

`School Risk` dùng để tránh silent academic debt.

* Green = ổn.
* Yellow = có deadline gần, requirement khó hiểu, chưa chắc rubric, hoặc understanding yếu.
* Red = deadline sát, exam gần, group blocked, điểm/rubric nguy hiểm.

Rule:

* Any Red => pause optional failure injection.
* Two Yellow => documentation-only homelab.
* Three Yellow => certification maintenance only.
* Group project dependency outranks optional lab.

Từ tháng 8 đến tháng 12, sheet này phải được xem trước khi chọn homelab work. Nếu trường đang Red mà vẫn chạy failure injection optional, bạn đang dùng roadmap sai.

## 10. How to Use Certification Sheet

Certification sheet không phải bảng "tôi học bao nhiêu giờ". Nó là bảng weak area và retest.

* Q1 ưu tiên CCNA.
* Q2 ưu tiên CKA.
* AWS SAA chỉ là bonus khi CCNA/CKA và trường ổn.
* Không dùng điểm practice để tự lừa mình; phải ghi weak area và retest.

Ví dụ tốt:

| Field | Example |
| ----- | ------- |
| Certification Track | CCNA |
| Domain / Topic | ACL order and default deny |
| Study Type | Practice Exam |
| Practice Score | 78 |
| Weak Area | ACL order |
| Retest Needed? | Yes |
| Status | Needs Retest |

Nếu score cao nhưng weak area không rõ, session đó chưa đủ giá trị.

## 11. How to Use Monthly Review

Cuối tháng mở `Monthly Review` và chấm 1-5:

* formal explanation quality;
* evidence quality;
* debugging discipline;
* diagram quality;
* postmortem quality;
* certification progress;
* restraint from tool collecting.

Đừng chấm theo cảm giác vui/buồn. Chấm theo artifact.

Kill List là bắt buộc. Mỗi tháng kill ít nhất một distraction:

* tool không dùng;
* document trùng;
* lab bỏ dở;
* script không rõ mục đích;
* roadmap phụ gây nhiễu.

Ví dụ Kill List tốt:

* "Archive old Kubernetes notes until Q2 starts."
* "Remove duplicated network diagram draft."
* "Stop evaluating new observability tools; current measurement is enough for Q1."

## 12. Example Week

### Monday

Theory mapping VLAN / 802.1Q / packet path.

Daily Log:

* Roadmap Phase: `Q1 Network and OS`
* Task Type: `Theory Mapping`
* Category: `Networking`
* System / Project: `VyOS / Router`
* Formal Concept: `IEEE 802.1Q tagging, broadcast domain`
* Action Taken: `Mapped client -> switch -> VyOS subinterface -> service path`
* Evidence Produced?: `Partial`
* Next Action: `Add tcpdump evidence`

### Tuesday

Break wrong default gateway.

Daily Log:

* Task Type: `Break / Failure Injection`
* Hypothesis / Goal: `Wrong gateway should fail off-subnet traffic while local subnet still works`
* Break?: `Yes`
* Measure?: `Yes`
* Fix?: `No`
* Document?: `No`
* Status: `Done`
* Next Action: `Measure route and packet capture`

### Wednesday

Measure `ip route`, `traceroute`, `tcpdump`.

Daily Log:

* Task Type: `Measure`
* Formal Concept: `Routing table lookup`
* Action Taken: `Captured route table, traceroute, ARP table, tcpdump`
* Result: `Traffic selected wrong next hop`
* Evidence Produced?: `Yes`
* Evidence Link / Path: path tới measurement note

### Thursday

Fix route config.

Daily Log:

* Task Type: `Fix`
* Formal Concept: `Default route restoration`
* Action Taken: `Restored correct gateway and compared before/after output`
* Result: `Connectivity restored and route path matched expected gateway`
* Fix?: `Yes`
* Document?: `Partial`

### Friday

Write lab report/postmortem.

Daily Log:

* Task Type: `Document`
* Category: `Documentation`
* Result: `Level 2 lab report created`
* Evidence Produced?: `Yes`
* Document?: `Yes`
* Next Action: `Clean topology diagram`

### Saturday

CCNA drill.

Daily Log:

* Task Type: `Certification Drill`
* Category: `Certification`
* Formal Concept: `Subnetting, static routing, ACL basics`
* Result: `Weak topics listed for retest`
* Evidence Produced?: `Partial`
* Next Action: `Retest ACL questions`

### Sunday

Weekly review.

Daily Log:

* Task Type: `Review`
* Category: `University` hoặc `Documentation`, tùy nội dung chính
* Action Taken: `Answered five review gate questions`
* Result: `Weekly review ready with best evidence link`
* Next Action: `Start next theory note`

Sau đó mở `Weekly Review` và viết review thật.

## 13. Common Mistakes

* Ghi task quá chung chung.
* Nhập nhiều giờ nhưng không có evidence.
* Để `Evidence Link / Path` trống.
* Quên `Formal Concept`.
* Biến Daily Log thành nhật ký cảm xúc.
* Bật nhiều WIP cùng lúc.
* Cố debug sau 10 PM.
* Dùng Chaos Mode quá muộn.
* Tạo dashboard đẹp nhưng không có decision.
* Học tool mới khi chưa có ADR/lý do.
* Chọn `Evidence Produced? = Yes` cho note chưa đủ path.
* Không ghi `What It Does Not Prove` trong Evidence Queue.

## 14. First 7 Days Setup

Trong 7 ngày đầu, đừng cố dùng hoàn hảo toàn bộ workbook.

Làm như sau:

* Chỉ nhập `Daily Log` đều.
* Không cố hoàn hảo `Evidence Queue`; raw evidence vẫn được.
* Cuối tuần mới fill `Weekly Review`.
* Sau tuần đầu kiểm tra Dashboard có phản ánh đúng không.
* Sửa dropdown/cột chỉ khi thật sự bất tiện.
* Nếu đang bận học, ghi `University Work`; đừng ép homelab mới.

Mục tiêu tuần đầu là tạo thói quen ghi evidence, không phải tối ưu spreadsheet.

## 15. Minimum Daily Standard

Mỗi ngày chỉ cần đủ:

* 1 task chính;
* 1 formal concept;
* 1 action taken;
* evidence status;
* time spent;
* energy/sleep;
* next action.

Nếu ngày đó bận học:

* ghi `University Work`;
* map với roadmap nếu có;
* không ép homelab lab mới.

Minimum good line:

> "University Work, C4 Context draft for student-feedback-system, mapped course deliverable to software architecture concept, 1.5h, evidence partial, next action: clean diagram."

Như vậy vẫn đúng roadmap hơn là cố mở một lab mới trong khi deadline trường đang đến gần.
