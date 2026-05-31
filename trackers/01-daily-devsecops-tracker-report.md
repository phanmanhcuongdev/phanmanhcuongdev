# Daily DevSecOps Tracker Report

## 1. Purpose

File Excel `01-daily-devsecops-tracker.xlsx` được thiết kế để vận hành roadmap DevSecOps hằng ngày, không phải để ghi chép cho đẹp. Nó buộc mỗi ngày học/lab phải đi qua các câu hỏi: làm gì, map với concept nào, có evidence không, có quá tải không, và cuối tuần có gì đủ tốt để review.

Mục tiêu chính:

* vận hành roadmap DevSecOps hằng ngày;
* chống học lan man và chống "tool collecting";
* ép mỗi việc học/lab có evidence;
* cân bằng homelab, certification và university workload;
* phát hiện quá tải bằng `Chaos Mode`, `School Risk`, `WIP Limit`;
* biến daily work thành weekly review, evidence queue và portfolio material.

Source of truth là `12-month-devsecops-roadmap.md`. Roadmap đặt luật: `No new tool collecting`, `Break -> Measure -> Fix -> Document`, mỗi lab phải có evidence, và nếu không chứng minh/reproduce được thì chưa được xem là xong/học được.

## 2. Design Principles

* **Evidence-first**: giờ học không đủ. Mỗi việc quan trọng cần có command transcript, log, packet capture, metric, config diff, diagram, lab report, postmortem hoặc ADR.
* **Break -> Measure -> Fix -> Document**: tracker tách rõ các cột `Break?`, `Measure?`, `Fix?`, `Document?` để tránh làm lab kiểu "sửa xong là thôi".
* **Foundation-first**: roadmap phase bắt đầu từ `Q1 Network and OS`, rồi đến `Q2 Kubernetes and Runtime`, `Q3 Database and Security`, `Q4 Production and Portfolio`.
* **Anti-tool-sprawl**: tracker có `Restraint From Tool Collecting`, WIP limit và Kill List để không mở thêm tool/lab khi chưa có lý do.
* **Weekly review gate**: Chủ nhật phải trả lời 5 câu review. Nếu câu "senior engineer reject gì?" chưa rõ, tuần đó chưa thật sự done.
* **School-heavy protection**: từ tháng 8 đến tháng 12, trường/GPA được bảo vệ bằng `School Risk` và `Chaos Mode`.
* **WIP limit**: cùng lúc chỉ active 1 university deliverable, 1 certification track, 1 homelab experiment/document.
* **Recovery is part of the system, not laziness**: sleep, recovery, stress và late-night debugging được track vì debugging khi kiệt sức tạo lỗi giả và academic debt.

## 3. Workbook Overview

Workbook thực tế có 11 worksheet, đúng tên sau: `Dashboard`, `Daily Log`, `Weekly Review`, `Evidence Queue`, `WIP Limit`, `Chaos Mode`, `Habit & Energy`, `Certification`, `School Risk`, `Monthly Review`, `Lookup`.

| Sheet | Purpose | Primary User Action | Output Produced |
| ----- | ------- | ------------------- | --------------- |
| Dashboard | Tổng hợp tuần hiện tại từ các sheet khác. | Đọc metric, alerts, status cards; không nhập daily data ở đây. | Weekly summary, roadmap balance, risk alerts. |
| Daily Log | Sheet nhập liệu chính cho công việc hằng ngày. | Thêm task chính mỗi ngày, chọn phase/type/category/status, ghi concept/action/result/evidence. | Nguồn dữ liệu cho Dashboard và Weekly Review. |
| Weekly Review | Review gate theo tuần. | Chủ nhật trả lời 5 câu review, link artifact tốt nhất, quyết định tuần sau. | Weekly decision, evidence count, labs completed. |
| Evidence Queue | Hàng đợi evidence để không thất lạc artifact. | Ghi evidence ID, type, level, path, what it proves/does not prove. | Raw evidence -> lab report/postmortem/portfolio material. |
| WIP Limit | Kiểm soát số việc active. | Ghi trạng thái university/certification/homelab hiện tại. | WIP status và action required. |
| Chaos Mode | Bảo vệ khi deadline/exam/sleep/lab failure va chạm. | Tick trigger Yes/No, chọn allowed/banned/recovery work. | Chaos Mode Off/Watch/On và scope giảm. |
| Habit & Energy | Theo dõi sleep, focus, stress, context switching, recovery. | Nhập sleep/focus/energy/stress mỗi ngày. | Tín hiệu quá tải cho decision cá nhân. |
| Certification | Theo dõi CCNA/CKA/AWS SAA. | Ghi track, topic, study type, score, weak area, retest. | Certification progress và weak area list. |
| School Risk | Academic risk register. | Ghi course, deadline, risk, required output, action this week. | School risk signal cho WIP/Chaos decisions. |
| Monthly Review | Review board cuối tháng. | Chấm điểm 7 tiêu chí, ghi kill list, artifact tốt nhất, quyết định tháng sau. | Monthly scorecard và scope decision. |
| Lookup | Danh sách dropdown và named ranges. | Chỉ chỉnh khi cần thay danh mục dropdown. | Data validation source. |

Không có sheet nào trong danh sách kỳ vọng bị thiếu.

## 4. Sheet-by-Sheet Specification

### Sheet: Dashboard

* **Purpose**: tổng quan tuần hiện tại. Dashboard không phải nơi nhập daily log.
* **Key columns/areas**: `Current Week Summary`, `Roadmap Balance`, `Status Cards`, `Alerts`, `Weekly Review Questions`.
* **What the user enters**: gần như không nhập tay. Dữ liệu đi vào từ `Daily Log`, `Weekly Review`, `Chaos Mode`, `School Risk`, `WIP Limit`.
* **What is calculated**: week start/end, total focus hours, homelab/certification/university/documentation hours, evidence items, labs completed, review gate status, chaos days, average energy/sleep, school risk, WIP status, roadmap balance theo task type, status cards và alerts.
* **Important dropdowns**: không có dropdown trên sheet này.
* **Important conditional formatting**: status cards đổi màu theo trạng thái tốt/cảnh báo/lỗi; alerts được highlight khi có nội dung.
* **How this sheet connects to other sheets**: dùng công thức `SUMIFS`, `COUNTIFS`, `AVERAGEIFS`, `INDEX/MATCH` từ các sheet khác.
* **Common mistakes to avoid**: sửa trực tiếp công thức; dùng số giờ cao để tự lừa mình khi evidence thấp; đọc dashboard mà không ra decision.

### Sheet: Daily Log

* **Purpose**: nguồn dữ liệu trung tâm của workbook.
* **Key columns**: `Date`, `Day`, `Week Number`, `Month`, `Roadmap Phase`, `Quarter`, `Task Title`, `Task Type`, `Category`, `System / Project`, `Formal Concept`, `Hypothesis / Goal`, `Action Taken`, `Result`, `Evidence Produced?`, `Evidence Link / Path`, `Break?`, `Measure?`, `Fix?`, `Document?`, `Time Spent Hours`, `Energy Level`, `Sleep Hours`, `School Risk Level`, `Chaos Mode?`, `Status`, `Notes`, `Next Action`.
* **What the user enters**: date, phase/type/category/project, task title, formal concept, hypothesis, action/result, evidence status/path, break/measure/fix/document flags, time/energy/sleep/risk/status/notes/next action.
* **What is calculated**: `Day`, `Week Number`, `Month`, `Quarter` được tính từ `Date` và `Roadmap Phase`.
* **Important dropdowns**: RoadmapPhase, TaskType, Category, SystemProject, EvidenceProduced, YesNoNA, EnergyLevel, SchoolRiskLevel, YesNo, Status.
* **Important conditional formatting**: evidence `No` với time >= 2h; school risk red/yellow; chaos mode yes; status done/blocked; low energy; sleep < 6.
* **How this sheet connects to other sheets**: Dashboard và Weekly Review đọc trực tiếp từ Daily Log.
* **Common mistakes to avoid**: ghi task quá chung chung; để `Formal Concept` trống; ghi `Evidence Produced? = Yes` nhưng không có path; nhập nhiều task nhỏ trong một dòng khiến review bị mờ.

Sample data hiện có 7 dòng từ 2026-05-25 đến 2026-05-31: theory mapping VLAN, break wrong default gateway, measure bằng route/traceroute/tcpdump, fix routing config, document postmortem, CCNA drill, weekly review/university mapping.

### Sheet: Weekly Review

* **Purpose**: review gate cuối tuần.
* **Key columns**: `Week Start`, `Week End`, `Main Roadmap Phase`, `Weekly Theme`, 5 câu review, links artifact, `Total Focus Hours`, `Evidence Count`, `Labs Completed`, `Certification Progress`, `School Risk Summary`, `Chaos Mode Triggered?`, `Review Status`, `Decision for Next Week`.
* **What the user enters**: week start/end, theme, câu trả lời review, links, certification/school summary, review status, decision.
* **What is calculated**: total focus hours, evidence count, labs completed từ `Daily Log`.
* **Important dropdowns**: RoadmapPhase, YesNo, ReviewStatus, DecisionNextWeek.
* **Important conditional formatting**: review `Done` và `Needs Fix` được highlight.
* **How this sheet connects to other sheets**: Dashboard đọc `Review Status`; Weekly Review tổng hợp Daily Log theo week start/end.
* **Common mistakes to avoid**: viết review cảm tính nhưng không link evidence; để `Decision for Next Week` chung chung; bỏ qua câu "hand-wavy".

### Sheet: Evidence Queue

* **Purpose**: giữ evidence không thất lạc.
* **Key columns**: `Evidence ID`, `Date`, `Related Task`, `Roadmap Phase`, `Evidence Type`, `Evidence Level`, `File / Link / Path`, `System / Project`, `Formal Concept`, `What It Proves`, `What It Does Not Prove`, `Needs Cleanup?`, `Portfolio Candidate?`, `Status`, `Notes`.
* **What the user enters**: mọi evidence đáng giữ, kể cả raw transcript/screenshot/log.
* **What is calculated**: không thấy công thức tự động trong sheet này.
* **Important dropdowns**: RoadmapPhase, EvidenceType, EvidenceLevel, SystemProject, YesNo, EvidenceQueueStatus.
* **Important conditional formatting**: Level 0 raw chưa reviewed, portfolio candidate, needs cleanup.
* **How this sheet connects to other sheets**: hiện tại chủ yếu là workflow thủ công từ Daily Log sang Evidence Queue; không có công thức tự động tạo evidence item.
* **Common mistakes to avoid**: chỉ ghi "screenshot" mà không ghi path; không ghi `What It Does Not Prove`; để Level 0 quá lâu không cleanup.

### Sheet: WIP Limit

* **Purpose**: chống context switching quá nhiều.
* **Key columns**: `Date`, active university/certification/homelab item, status từng item, `Total Active Items`, `WIP Limit Status`, `Action Required`, `Notes`.
* **What the user enters**: tên deliverable/track/experiment và trạng thái.
* **What is calculated**: `Total Active Items`, `WIP Limit Status`, `Action Required`.
* **Important dropdowns**: WorkStatus, WIPStatus, ActionRequired.
* **Important conditional formatting**: OK/Warning/Violation.
* **How this sheet connects to other sheets**: `Action Required` kiểm tra `School Risk` cùng ngày; Dashboard đọc WIP status mới nhất.
* **Common mistakes to avoid**: đánh dấu nhiều thứ `Active`; dùng `Planned` như `Active`; không pause homelab khi school risk tăng.

### Sheet: Chaos Mode

* **Purpose**: giảm scope khi deadline/exam/sleep/lab failure vượt ngưỡng.
* **Key columns**: các trigger Yes/No, `Chaos Mode Status`, `Allowed Work`, `Banned Work`, `Recovery Action`, `Notes`.
* **What the user enters**: trigger Yes/No, allowed/banned work, recovery action.
* **What is calculated**: `Chaos Mode Status` = On nếu các trigger deadline/exam/lab/group là Yes; Watch nếu sleep/fatigue trigger.
* **Important dropdowns**: YesNo, ChaosModeStatus, AllowedWork, BannedWork, RecoveryAction.
* **Important conditional formatting**: On/Watch; Banned Work trống khi On.
* **How this sheet connects to other sheets**: Dashboard đếm số ngày `Chaos Mode Status = On`. Hiện tại Chaos Mode không tự đọc trực tiếp từ Daily Log/Habit & Energy; trigger cần nhập tay.
* **Common mistakes to avoid**: bật Chaos Mode quá muộn; để On mà vẫn làm failure injection; không ghi banned work.

### Sheet: Habit & Energy

* **Purpose**: theo dõi điều kiện vận hành cá nhân.
* **Key columns**: `Date`, `Sleep Hours`, `Focus Hours`, `Deep Work Blocks`, `Exercise / Run?`, `Energy Level`, `Stress Level`, `Context Switching Level`, `Late Night Debugging?`, `Recovery Done?`, `Notes`.
* **What the user enters**: sleep, focus, energy, stress, context switching, recovery.
* **What is calculated**: không thấy công thức tự động trong sheet này.
* **Important dropdowns**: YesNo, EnergyLevel, StressLevel, ContextSwitchingLevel.
* **Important conditional formatting**: sleep < 6; late-night debugging; high stress; high context switching; high stress + no recovery.
* **How this sheet connects to other sheets**: intended workflow là hỗ trợ Dashboard/Chaos decisions. Trong file hiện tại, Dashboard tính average energy/sleep từ `Daily Log`, không phải từ `Habit & Energy`.
* **Common mistakes to avoid**: chỉ ghi focus hours mà bỏ sleep/stress; xem recovery là "mất thời gian".

### Sheet: Certification

* **Purpose**: track CCNA/CKA/AWS SAA theo discipline, không chạy theo exam ngẫu hứng.
* **Key columns**: `Date`, `Certification Track`, `Domain / Topic`, `Study Type`, `Time Spent Hours`, `Practice Score`, `Weak Area`, `Retest Needed?`, `Evidence Link`, `Status`, `Notes`.
* **What the user enters**: study session, score, weak area, retest, evidence link.
* **What is calculated**: không thấy công thức tự động trong sheet này.
* **Important dropdowns**: CertificationTrack, StudyType, YesNo, Status.
* **Important conditional formatting**: AWS SAA không deferred được highlight; Needs Retest được highlight.
* **How this sheet connects to other sheets**: intended workflow là đưa progress vào Weekly Review/Monthly Review. Trong file hiện tại chưa có công thức tự động kéo Certification vào Monthly Review.
* **Common mistakes to avoid**: học AWS SAA khi CCNA/CKA và school chưa ổn; ghi practice score nhưng không ghi weak area/retest.

### Sheet: School Risk

* **Purpose**: academic risk register, đặc biệt quan trọng từ tháng 8 đến tháng 12.
* **Key columns**: `Date`, `Course`, `Current Risk`, `Next Deadline`, `Days Until Deadline`, `Required Output`, `Roadmap Mapping`, `Action This Week`, `Group Dependency?`, `Status`, `Notes`.
* **What the user enters**: course, risk, deadline, output, mapping, action, dependency/status.
* **What is calculated**: `Days Until Deadline = Next Deadline - Date`.
* **Important dropdowns**: SchoolRiskLevel, YesNo, SchoolStatus.
* **Important conditional formatting**: deadline <= 7 và chưa submitted; red/yellow risk; group dependency chưa submitted.
* **How this sheet connects to other sheets**: Dashboard tính School Risk theo tuần; WIP Limit dùng School Risk để ưu tiên `Finish School Work First`.
* **Common mistakes to avoid**: đợi đến khi deadline sát mới nhập; không map school deliverable vào roadmap artifact; coi group dependency là optional.

### Sheet: Monthly Review

* **Purpose**: review board cuối tháng.
* **Key columns**: `Month`, `Roadmap Phase`, 7 score columns, `Average Score`, `Kill List Item`, `Best Artifact`, `Weakest Area`, `Decision for Next Month`, `Notes`.
* **What the user enters**: điểm 1-5, kill list, artifact tốt nhất, weakest area, decision.
* **What is calculated**: `Average Score`.
* **Important dropdowns**: RoadmapPhase, MonthlyDecision.
* **Important conditional formatting**: average score < 3, 3-4, >= 4.
* **How this sheet connects to other sheets**: intended workflow là review tổng hợp từ Weekly Review, Evidence Queue và Certification. Hiện tại phần lớn cần nhập tay.
* **Common mistakes to avoid**: chấm điểm rộng tay; không kill distraction; chỉ ghi "continue" mà không chỉ rõ scope.

### Sheet: Lookup

* **Purpose**: nguồn danh sách dropdown.
* **Key columns**: `List Name`, `Value`.
* **What the user enters**: chỉ chỉnh khi cần thay danh mục dropdown.
* **What is calculated**: không có công thức.
* **Important dropdowns**: không có dropdown trong chính sheet này; nó cấp named ranges cho các sheet khác.
* **Important conditional formatting**: không có.
* **How this sheet connects to other sheets**: các data validation dùng named range như RoadmapPhase, TaskType, Category, EvidenceLevel, CertificationTrack.
* **Common mistakes to avoid**: xóa hoặc đổi tên list làm hỏng dropdown; thêm value trùng nghĩa.

## 5. Data Flow

**Current implementation**

* `Daily Log -> Dashboard`: có công thức tổng hợp focus hours, evidence count, labs completed, average energy/sleep, roadmap balance.
* `Daily Log -> Weekly Review`: có công thức tính total focus hours, evidence count, labs completed theo week start/end.
* `Daily Log -> Evidence Queue`: chưa tự động; người dùng phải copy/ghi evidence đáng giữ vào Evidence Queue.
* `Daily Log + School Risk -> Chaos Mode`: hiện tại Chaos Mode dùng trigger nhập tay. Dashboard đọc Chaos Mode days, nhưng Chaos Mode không tự tính từ Daily Log/Habit & Energy.
* `Habit & Energy -> Dashboard`: intended workflow có, nhưng file hiện tại Dashboard lấy average energy/sleep từ `Daily Log`, không lấy từ `Habit & Energy`.
* `Certification -> Monthly Review`: chưa có công thức tự động; user tự tổng hợp progress vào Monthly Review.
* `School Risk -> WIP/Chaos decisions`: WIP Limit có công thức ưu tiên school risk cùng ngày; Chaos Mode chưa tự kéo từ School Risk.
* `Evidence Queue -> Portfolio material`: workflow thủ công qua `Portfolio Candidate?`, `Evidence Level`, `Status`.

**Intended workflow**

Daily Log là log vận hành. Evidence Queue là kho artifact. Weekly Review là cổng kiểm tra chất lượng tuần. Dashboard là nơi đọc tín hiệu. Monthly Review là nơi cắt scope và nâng artifact.

**Manual step needed**

Sau mỗi task có evidence thật, bạn cần thêm dòng vào Evidence Queue. Cuối tuần cần tự viết Weekly Review. Cuối tháng cần tự chấm Monthly Review. Chaos Mode trigger cũng cần nhập trung thực thay vì chờ workbook tự suy luận.

## 6. Status and Risk Logic

* `Evidence Produced? = Yes`: có artifact đủ link/path, có thể dùng để review.
* `Evidence Produced? = Partial`: có raw/partial note/log/screenshot, chưa đủ sạch nhưng không mất dấu.
* `Evidence Produced? = No`: chưa có bằng chứng. Nếu spent time >= 2h thì đây là red flag.
* `School Risk = Green`: course ổn, chưa có deadline/rubric/dependency đáng lo.
* `School Risk = Yellow`: có deadline gần, requirement chưa rõ, weak understanding, hoặc dependency cần theo dõi.
* `School Risk = Red`: deadline sát, exam/quiz/rubric nguy hiểm, group blocked, hoặc course có nguy cơ ảnh hưởng GPA.
* `Chaos Mode = Off`: làm theo cadence bình thường.
* `Chaos Mode = Watch`: giảm tham vọng, ưu tiên documentation/evidence parking/recovery.
* `Chaos Mode = On`: dừng failure injection optional và infrastructure change không cần thiết.
* `WIP Status = OK`: số việc active dưới ngưỡng.
* `WIP Status = Warning`: đã chạm ngưỡng, nên documentation-only hoặc giảm scope.
* `WIP Status = Violation`: quá nhiều việc active, phải drop/pause task.
* `Review Status = Not Started`: chưa review.
* `Review Status = In Progress`: đang review, chưa đủ gate.
* `Review Status = Done`: tuần có câu trả lời và evidence đủ dùng.
* `Review Status = Needs Fix`: review phát hiện chỗ hand-wavy cần sửa.
* Evidence Level 0-4: Level 0 raw; Level 1 cleaned observation; Level 2 lab report; Level 3 postmortem/ADR; Level 4 portfolio case study.

## 7. How This Supports the 12-Month Roadmap

* **Q1 Network and OS**: Daily Log và Evidence Queue hỗ trợ packet path, VLAN, route table, default gateway, CCNA drills.
* **Q2 Kubernetes and Runtime**: Task Type và Evidence Type đủ để track pods/services/probes/events/logs/runbooks khi bước vào CKA.
* **Q3 Database and Security**: Evidence Queue có Log, Packet Capture, Metric Graph, Config Diff, Postmortem, ADR để support database/security/failure reports.
* **Q4 Production and Portfolio**: Portfolio Candidate và Monthly Review giúp nâng Level 2/3 thành Level 4 case study.
* **School-heavy mode**: School Risk, WIP Limit, Chaos Mode bảo vệ GPA và tránh silent academic debt từ 2026-08 đến 2026-12.
* **Monthly review board**: Monthly Review bám scorecard roadmap: formal explanation, evidence quality, debugging discipline, diagram quality, postmortem quality, certification progress, restraint from tool collecting.

## 8. Strengths of the Current Workbook

* Workbook có nhiều sheet tách vai trò rõ, không nhét nhiều bảng vào một worksheet.
* Các sheet nhập liệu chính có Excel Table.
* Có dropdown validation rộng: Daily Log 13 nhóm, Evidence Queue 7, Chaos Mode 10, v.v.
* Có Dashboard dùng công thức thật từ sheet khác.
* Có sample data Daily Log 7 ngày và Habit & Energy 7 ngày.
* Có evidence tracking riêng bằng Evidence Queue.
* Có School Risk, Chaos Mode, WIP Limit để bảo vệ khỏi quá tải và học lan man.
* Có Lookup sheet tập trung danh sách dropdown.
* Có conditional formatting trên các vùng rủi ro chính.

## 9. Limitations / Things to Verify

* Dashboard lấy average energy/sleep từ `Daily Log`, không lấy từ `Habit & Energy`. Nếu bạn nhập Habit & Energy nhưng quên nhập Daily Log, Dashboard không phản ánh phần đó.
* `Evidence Queue` không tự sinh từ `Daily Log`; phải nhập tay evidence quan trọng.
* `Chaos Mode` không tự kéo trigger từ `School Risk` hoặc `Habit & Energy`; trigger cần nhập tay.
* `Certification` chưa tự tổng hợp sang `Monthly Review`.
* `Monthly Review` phần lớn là manual review board, không phải dashboard tự động.
* Conditional formatting tồn tại nhưng inspection chỉ đọc được vùng áp dụng, không diễn giải đầy đủ từng rule bằng mắt như Excel UI.
* Dropdown dựa trên named ranges trong Lookup; nếu đổi tên list trong Lookup hoặc xóa named range, validation có thể hỏng.
* Workbook có sample paths tới `E:\Roadmaps\evidence\...`; cần tạo file evidence thật sau này, nếu không link chỉ là placeholder.

## 10. Recommended Operating Rule

* Mỗi ngày nhập `Daily Log`.
* Mỗi evidence đáng giữ thì ghi vào `Evidence Queue`.
* Mỗi Chủ nhật điền `Weekly Review`.
* Mỗi tháng điền `Monthly Review`.
* Khi `School Risk = Red`, cấm failure injection optional.
* Khi `Chaos Mode = On`, chỉ làm school deadline, service stability, evidence parking, documentation-only hoặc recovery.
* Không thêm tool mới nếu không bắt buộc bởi CCNA/CKA/AWS SAA, không thay tool cũ, hoặc chưa có ADR.
* Nếu hệ thống chạy nhưng không chứng minh được vì sao, coi như chưa xong.
* Nếu hệ thống lỗi nhưng không reproduce được lỗi, coi như chưa học được.
