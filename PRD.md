# LetsPay - Product Requirements Document (PRD)

## 문서 정보

| 항목 | 내용 |
|------|------|
| **프로젝트명** | LetsPay (렛츠페이) |
| **문서 버전** | v1.0 |
| **작성일** | 2026-01-30 |
| **상태** | Draft |

---

## 1. 서비스 개요

### 1.1 서비스 정의

LetsPay는 **비대면 결제가 필요한 모든 사업장**을 위한 모바일 청구서 발송 및 수납 관리 플랫폼입니다.

### 1.2 핵심 가치 제안 (Value Proposition)

> "언제 어디서나, 쉽고 빠른 비대면 청구/결제"

- **사업자**: 간편한 청구서 발송 및 자동화된 수납 관리
- **고객**: 앱 설치 없이 알림톡/문자로 즉시 결제

### 1.3 타겟 고객

| 우선순위 | 타겟 | 특징 |
|----------|------|------|
| 1순위 | 학원/교습소 | 정기 수강료 청구, 학생 관리 필요 |
| 1순위 | 독서실/스터디카페 | 월 이용료 정기 청구 |
| 2순위 | 피트니스/요가원 | 회원권/PT 비용 청구 |
| 2순위 | 병원/의원 | 진료비 비대면 청구 |
| 3순위 | 프리랜서 | 용역비 청구 |
| 3순위 | 소상공인 | 비대면 결제 니즈 |

### 1.4 비즈니스 목표

| 목표 | KPI | 목표치 (1년) |
|------|-----|-------------|
| 사업자 가입 | 가입자 수 | 10,000명 |
| 거래액 | 월 거래액 | 50억원 |
| 활성 사용자 | MAU | 5,000명 |
| 고객 만족도 | NPS | 50점 이상 |

---

## 2. 기능 요구사항

### 2.1 사용자 유형

```
┌─────────────────────────────────────────────────────────┐
│                     LetsPay 시스템                       │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  [사업자]              [시스템]              [고객]      │
│     │                     │                    │        │
│  - 회원가입            - 청구서 발송         - 결제      │
│  - 청구서 작성         - 결제 처리           - 결제내역  │
│  - 수납 관리           - 알림 발송                       │
│  - 매출 분석           - 정산 처리                       │
│  - 고객 관리                                             │
│                                                         │
│  [관리자]                                                │
│  - 사업자 관리                                           │
│  - 정산 관리                                             │
│  - 시스템 모니터링                                       │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### 2.2 핵심 기능 목록

#### 2.2.1 인증 및 회원 관리

| ID | 기능 | 설명 | 우선순위 |
|----|------|------|----------|
| AUTH-001 | 회원가입 | 이메일/휴대폰 인증 기반 회원가입 | P0 |
| AUTH-002 | 로그인 | 이메일/소셜 로그인 (카카오, 네이버, 구글) | P0 |
| AUTH-003 | 사업자 인증 | 사업자등록번호 검증 및 인증 | P0 |
| AUTH-004 | 비밀번호 찾기 | 이메일/SMS 기반 비밀번호 재설정 | P0 |
| AUTH-005 | 프로필 관리 | 사업장 정보, 정산 계좌 관리 | P1 |

#### 2.2.2 청구서 발송

| ID | 기능 | 설명 | 우선순위 |
|----|------|------|----------|
| BILL-001 | 단건 발송 | 개별 청구서 작성 및 발송 | P0 |
| BILL-002 | 대량 발송 | 엑셀 업로드를 통한 대량 발송 | P0 |
| BILL-003 | 예약 발송 | 특정 날짜/시간에 자동 발송 | P1 |
| BILL-004 | 정기 발송 | 주기적 자동 발송 (매월/매주) | P1 |
| BILL-005 | 청구서 템플릿 | 자주 사용하는 청구서 템플릿 저장 | P2 |
| BILL-006 | 청구서 파기 | 발송된 청구서 취소/파기 | P1 |
| BILL-007 | 재발송 | 미결제 청구서 재발송 | P1 |
| BILL-008 | 알림톡 발송 | 카카오 알림톡으로 청구서 발송 | P0 |
| BILL-009 | SMS 발송 | 문자 메시지로 청구서 발송 | P0 |
| BILL-010 | 안내 메시지 | 청구서에 커스텀 메시지 추가 | P2 |

#### 2.2.3 결제 처리

| ID | 기능 | 설명 | 우선순위 |
|----|------|------|----------|
| PAY-001 | 청구서 조회 | 고객이 링크로 청구서 확인 | P0 |
| PAY-002 | 카드 결제 | 신용/체크카드 결제 | P0 |
| PAY-003 | 간편결제 | 카카오페이, 네이버페이, 토스페이 등 | P0 |
| PAY-004 | 삼성페이/애플페이 | 모바일 페이 지원 | P1 |
| PAY-005 | 지역화폐 | 지역화폐 결제 지원 | P2 |
| PAY-006 | 자동결제 | 정기 자동결제 등록 | P1 |
| PAY-007 | 부분결제 | 청구금액 일부만 결제 | P2 |
| PAY-008 | 결제 취소 | 결제 취소 및 환불 처리 | P0 |
| PAY-009 | 청구서 전달 | 타인에게 청구서 공유 (대리결제) | P2 |

#### 2.2.4 수납/매출 관리

| ID | 기능 | 설명 | 우선순위 |
|----|------|------|----------|
| MGMT-001 | 수납 현황 | 실시간 수납 현황 조회 | P0 |
| MGMT-002 | 미수금 관리 | 미결제 청구서 관리 | P0 |
| MGMT-003 | 매출 대시보드 | 일/주/월별 매출 현황 차트 | P0 |
| MGMT-004 | 매출 보고서 | 기간별 매출 보고서 다운로드 | P1 |
| MGMT-005 | 정산 내역 | PG사 정산 내역 조회 | P0 |
| MGMT-006 | 결제 알림 | 실시간 결제 완료 알림 (푸시/앱) | P0 |
| MGMT-007 | 통계 분석 | 고객별/기간별 분석 리포트 | P2 |

#### 2.2.5 고객 관리

| ID | 기능 | 설명 | 우선순위 |
|----|------|------|----------|
| CRM-001 | 고객 등록 | 고객 정보 수동 등록 | P0 |
| CRM-002 | 고객 목록 | 등록된 고객 목록 조회/검색 | P0 |
| CRM-003 | 고객 그룹 | 고객 그룹화 (태그, 카테고리) | P1 |
| CRM-004 | 결제 이력 | 고객별 결제 내역 조회 | P0 |
| CRM-005 | 연락처 가져오기 | 휴대폰 연락처 동기화 (앱) | P1 |
| CRM-006 | 엑셀 가져오기 | 엑셀 파일로 고객 일괄 등록 | P1 |
| CRM-007 | 학생/회원 관리 | 교육기관용 학생 관리 기능 | P1 |

#### 2.2.6 현금영수증

| ID | 기능 | 설명 | 우선순위 |
|----|------|------|----------|
| RCP-001 | 자동 발급 | 결제 시 현금영수증 자동 발급 | P0 |
| RCP-002 | 수동 발급 | 현금 수납 건 수동 발급 | P1 |
| RCP-003 | 발급 내역 | 현금영수증 발급 내역 조회 | P0 |
| RCP-004 | 취소 | 현금영수증 취소 처리 | P1 |

#### 2.2.7 오프라인 결제 (Phase 2)

| ID | 기능 | 설명 | 우선순위 |
|----|------|------|----------|
| POS-001 | 블루투스 단말기 | BT 카드단말기 연동 | P2 |
| POS-002 | 현장 결제 | 대면 카드 결제 처리 | P2 |
| POS-003 | 통합 매출 | 온/오프라인 매출 통합 관리 | P2 |

---

## 3. 상세 기능 명세

### 3.1 청구서 발송 플로우

```
[사업자 - 청구서 작성]
         │
         ▼
┌─────────────────────┐
│  1. 발송 유형 선택   │
│  - 단건 / 대량      │
│  - 즉시 / 예약 / 정기│
└─────────────────────┘
         │
         ▼
┌─────────────────────┐
│  2. 고객 선택       │
│  - 직접 입력        │
│  - 고객 목록 선택   │
│  - 엑셀 업로드      │
└─────────────────────┘
         │
         ▼
┌─────────────────────┐
│  3. 청구 정보 입력  │
│  - 청구 금액        │
│  - 청구 사유/품목   │
│  - 면/과세 선택     │
│  - 안내 메시지      │
└─────────────────────┘
         │
         ▼
┌─────────────────────┐
│  4. 발송 채널 선택  │
│  - 알림톡 (기본)    │
│  - SMS (대체)       │
└─────────────────────┘
         │
         ▼
┌─────────────────────┐
│  5. 미리보기 & 발송 │
└─────────────────────┘
```

### 3.2 고객 결제 플로우

```
[고객 - 결제]
         │
         ▼
┌─────────────────────┐
│  1. 알림톡/SMS 수신 │
│  - 결제 링크 클릭   │
└─────────────────────┘
         │
         ▼
┌─────────────────────┐
│  2. 청구서 확인     │
│  - 사업자 정보      │
│  - 청구 금액/사유   │
│  - 안내 메시지      │
│  (앱 설치 불필요)   │
└─────────────────────┘
         │
         ▼
┌─────────────────────┐
│  3. 결제 수단 선택  │
│  - 카드 직접 입력   │
│  - 간편결제 선택    │
│  - 자동결제 등록    │
└─────────────────────┘
         │
         ▼
┌─────────────────────┐
│  4. 결제 완료       │
│  - 결제 완료 화면   │
│  - 영수증 확인      │
└─────────────────────┘
         │
         ▼
[사업자 - 실시간 알림 수신]
```

### 3.3 청구서 데이터 모델

```typescript
interface Bill {
  id: string;                    // 청구서 고유 ID
  merchantId: string;            // 사업자 ID
  customerId: string;            // 고객 ID

  // 청구 정보
  amount: number;                // 청구 금액
  title: string;                 // 청구 제목
  description?: string;          // 청구 상세 설명
  items?: BillItem[];            // 청구 항목 목록

  // 세금 정보
  taxType: 'TAX' | 'TAX_FREE';   // 과세/면세
  supplyAmount?: number;         // 공급가액
  taxAmount?: number;            // 세액

  // 발송 정보
  sendType: 'IMMEDIATE' | 'SCHEDULED' | 'RECURRING';
  sendChannel: 'ALIMTALK' | 'SMS' | 'BOTH';
  scheduledAt?: Date;            // 예약 발송 시간
  recurringRule?: RecurringRule; // 정기 발송 규칙

  // 상태
  status: BillStatus;
  sentAt?: Date;                 // 발송 시간
  paidAt?: Date;                 // 결제 완료 시간
  cancelledAt?: Date;            // 취소 시간

  // 결제 정보
  paymentId?: string;            // 결제 ID
  paymentMethod?: string;        // 결제 수단

  // 메타데이터
  message?: string;              // 안내 메시지
  expiresAt?: Date;              // 청구서 만료일
  createdAt: Date;
  updatedAt: Date;
}

type BillStatus =
  | 'DRAFT'      // 작성중
  | 'PENDING'    // 발송 대기
  | 'SENT'       // 발송 완료
  | 'VIEWED'     // 고객 확인
  | 'PAID'       // 결제 완료
  | 'CANCELLED'  // 취소됨
  | 'EXPIRED';   // 만료됨

interface BillItem {
  name: string;                  // 품목명
  quantity: number;              // 수량
  unitPrice: number;             // 단가
  amount: number;                // 금액
}

interface RecurringRule {
  frequency: 'WEEKLY' | 'MONTHLY';
  dayOfWeek?: number;            // 0-6 (일-토)
  dayOfMonth?: number;           // 1-31
  startDate: Date;
  endDate?: Date;
}
```

### 3.4 API 엔드포인트 설계

#### 인증 API

| Method | Endpoint | 설명 |
|--------|----------|------|
| POST | `/api/auth/signup` | 회원가입 |
| POST | `/api/auth/login` | 로그인 |
| POST | `/api/auth/logout` | 로그아웃 |
| POST | `/api/auth/refresh` | 토큰 갱신 |
| POST | `/api/auth/verify-business` | 사업자 인증 |
| POST | `/api/auth/password/reset` | 비밀번호 재설정 |

#### 청구서 API

| Method | Endpoint | 설명 |
|--------|----------|------|
| GET | `/api/bills` | 청구서 목록 조회 |
| POST | `/api/bills` | 청구서 생성 |
| GET | `/api/bills/:id` | 청구서 상세 조회 |
| PUT | `/api/bills/:id` | 청구서 수정 |
| DELETE | `/api/bills/:id` | 청구서 삭제 |
| POST | `/api/bills/:id/send` | 청구서 발송 |
| POST | `/api/bills/:id/cancel` | 청구서 취소 |
| POST | `/api/bills/:id/resend` | 청구서 재발송 |
| POST | `/api/bills/bulk` | 대량 청구서 발송 |

#### 결제 API

| Method | Endpoint | 설명 |
|--------|----------|------|
| GET | `/api/payments/:billId` | 청구서 결제 페이지 |
| POST | `/api/payments/:billId/pay` | 결제 처리 |
| POST | `/api/payments/:id/cancel` | 결제 취소 |
| GET | `/api/payments/history` | 결제 내역 조회 |

#### 고객 API

| Method | Endpoint | 설명 |
|--------|----------|------|
| GET | `/api/customers` | 고객 목록 |
| POST | `/api/customers` | 고객 등록 |
| GET | `/api/customers/:id` | 고객 상세 |
| PUT | `/api/customers/:id` | 고객 수정 |
| DELETE | `/api/customers/:id` | 고객 삭제 |
| POST | `/api/customers/import` | 고객 일괄 등록 |

#### 매출/정산 API

| Method | Endpoint | 설명 |
|--------|----------|------|
| GET | `/api/dashboard` | 대시보드 데이터 |
| GET | `/api/reports/sales` | 매출 보고서 |
| GET | `/api/reports/settlements` | 정산 내역 |
| GET | `/api/reports/export` | 보고서 다운로드 |

---

## 4. 비기능 요구사항

### 4.1 성능 요구사항

| 항목 | 요구사항 |
|------|----------|
| 페이지 로딩 | 3초 이내 (LCP) |
| API 응답 시간 | 500ms 이내 (p95) |
| 동시 사용자 | 1,000명 이상 |
| 청구서 발송 | 1,000건/분 처리 |
| 시스템 가용성 | 99.9% SLA |

### 4.2 보안 요구사항

| 항목 | 요구사항 |
|------|----------|
| 통신 암호화 | HTTPS (TLS 1.3) |
| 인증 | JWT + Refresh Token |
| 개인정보 암호화 | AES-256 (휴대폰, 카드번호) |
| PCI-DSS | PG사 연동으로 준수 |
| 접근 제어 | RBAC (역할 기반 접근 제어) |
| 감사 로그 | 모든 주요 활동 로깅 |

### 4.3 확장성 요구사항

- 수평적 확장 가능한 아키텍처
- 마이크로서비스 전환 가능 구조
- 멀티 테넌트 지원

---

## 5. 기술 스택

### 5.1 프론트엔드

| 구분 | 기술 | 선정 이유 |
|------|------|----------|
| Build Tool | **Vite** | 빠른 개발 서버, HMR |
| Framework | **React 18** | 컴포넌트 기반, 풍부한 생태계 |
| Language | TypeScript | 타입 안정성 |
| Styling | Tailwind CSS | 빠른 개발, 일관된 디자인 |
| UI Library | **shadcn/ui** | 커스터마이징 용이, 모던 디자인 |
| State (전역) | **Zustand** | 경량, 간단한 API |
| State (서버) | **TanStack Query** | 서버 상태 관리, 캐싱 |
| Form | React Hook Form + Zod | 폼 검증 |
| Chart | Recharts | 매출 차트 |
| Router | React Router v6 | SPA 라우팅 |
| 배포 | **Vercel** | 자동 배포, Vite 최적화 |

### 5.2 백엔드

| 구분 | 기술 | 선정 이유 |
|------|------|----------|
| Framework | **FastAPI** | 빠른 성능, 자동 API 문서화, async 지원 |
| Language | **Python 3.11+** | 생산성, 풍부한 라이브러리 |
| ORM | SQLAlchemy 2.0 | 비동기 지원, 성숙한 생태계 |
| Validation | Pydantic v2 | 데이터 검증, FastAPI 통합 |
| Task Queue | Celery / ARQ | 비동기 작업 (예약 발송, 정기 발송) |
| 배포 | **Railway** | 쉬운 배포, 자동 스케일링, Docker 지원 |

### 5.3 데이터베이스 & 인프라

| 구분 | 기술 | 선정 이유 |
|------|------|----------|
| Database | **Supabase (PostgreSQL)** | 관리형 DB, 실시간 기능, Row Level Security |
| Auth | **Supabase Auth** | 소셜 로그인 내장, DB 통합 |
| Storage | Supabase Storage | 파일 저장, S3 호환 API |
| Cache | Upstash Redis | 서버리스 Redis, Railway 통합 가능 |
| CDN | Vercel Edge Network | 정적 자산 캐싱, 글로벌 배포 |
| Monitoring | Sentry | 에러 추적, 성능 모니터링 |

### 5.4 인증 (Supabase Auth)

| 구분 | 내용 |
|------|------|
| 기본 인증 | 이메일/비밀번호 |
| 소셜 로그인 | **카카오, 네이버, 구글** |
| 세션 관리 | JWT (Supabase 내장) |
| 비밀번호 재설정 | 이메일 기반 Magic Link |

### 5.5 외부 서비스 연동

| 서비스 | 제공사 | 용도 |
|--------|--------|------|
| PG (결제) | **토스페이먼츠** | 카드/간편결제 (카카오페이, 네이버페이, 토스페이 등) |
| 알림톡/SMS | **솔라피 (Solapi)** | 카카오 알림톡 + SMS 통합 발송 |
| 사업자 인증 | 국세청 API / 공공데이터포털 | 사업자등록번호 진위확인 |
| 현금영수증 | 토스페이먼츠 (PG 연동) | 현금영수증 발급 |

### 5.6 개발 도구

| 구분 | 기술 |
|------|------|
| 패키지 관리 (FE) | pnpm |
| 패키지 관리 (BE) | Poetry / uv |
| 린팅 (FE) | ESLint + Prettier |
| 린팅 (BE) | Ruff + Black |
| API 문서 | Swagger UI (FastAPI 자동 생성) |
| 테스트 (FE) | Vitest + Testing Library |
| 테스트 (BE) | pytest + httpx |
| 버전 관리 | Git + GitHub |

### 5.7 프로젝트 구조

```
letspay/
├── frontend/                 # React + Vite (Vercel 배포)
│   ├── src/
│   │   ├── components/       # UI 컴포넌트
│   │   ├── pages/            # 페이지 컴포넌트
│   │   ├── hooks/            # 커스텀 훅
│   │   ├── stores/           # Zustand 스토어
│   │   ├── services/         # API 호출
│   │   ├── types/            # TypeScript 타입
│   │   └── utils/            # 유틸리티
│   ├── package.json
│   └── vite.config.ts
│
├── backend/                  # FastAPI (Railway 배포)
│   ├── app/
│   │   ├── api/              # API 라우터
│   │   ├── core/             # 설정, 보안
│   │   ├── models/           # SQLAlchemy 모델
│   │   ├── schemas/          # Pydantic 스키마
│   │   ├── services/         # 비즈니스 로직
│   │   └── utils/            # 유틸리티
│   ├── pyproject.toml
│   └── Dockerfile
│
└── docs/                     # 문서
```

---

## 6. 시스템 아키텍처

### 6.1 전체 아키텍처

```
┌─────────────────────────────────────────────────────────────────┐
│                         클라이언트                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   [React SPA]              [모바일 웹]         [고객 결제 페이지] │
│   (사업자 관리)            (반응형)            (PWA)             │
│   Vercel 배포              Vercel 배포         Vercel 배포       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
            ┌─────────────────┴─────────────────┐
            ▼                                   ▼
┌───────────────────────┐           ┌───────────────────────────┐
│    Supabase Auth      │           │     FastAPI Backend       │
│    (인증 서비스)       │           │     (Railway 배포)         │
├───────────────────────┤           ├───────────────────────────┤
│ - 이메일/비밀번호     │           │                           │
│ - 소셜 로그인         │           │  /api/bills      청구서   │
│   (카카오,네이버,구글) │           │  /api/payments   결제     │
│ - JWT 토큰 관리       │           │  /api/customers  고객     │
│ - 비밀번호 재설정     │           │  /api/dashboard  대시보드 │
│                       │           │  /api/receipts   영수증   │
└───────────────────────┘           │                           │
            │                       │  [Celery Worker]          │
            │                       │  - 예약 발송              │
            │                       │  - 정기 발송              │
            │                       │  - 알림 처리              │
            │                       └───────────────────────────┘
            │                                   │
            └─────────────────┬─────────────────┘
                              │
┌─────────────────────────────────────────────────────────────────┐
│                        Supabase                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   [PostgreSQL]          [Storage]           [Realtime]          │
│   (메인 DB)             (파일 저장)          (실시간 알림)        │
│                                                                 │
│   - merchants           - 청구서 첨부        - 결제 알림         │
│   - customers           - 로고 이미지        - 상태 변경         │
│   - bills                                                       │
│   - payments                                                    │
│   - cash_receipts                                               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────────┐
│                     External Services                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   [토스페이먼츠]         [솔라피 Solapi]       [공공데이터포털]   │
│   - 카드 결제            - 카카오 알림톡       - 사업자 진위확인  │
│   - 간편결제             - SMS 문자 발송                         │
│   - 현금영수증           - 발송 결과 조회                        │
│   - 빌링키 (자동결제)                                            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 6.2 배포 구성

```
┌─────────────────────────────────────────────────────────────┐
│                      Vercel                                  │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              React + Vite (Frontend)                 │    │
│  │  - 사업자 대시보드                                   │    │
│  │  - 고객 결제 페이지                                  │    │
│  │  - 자동 HTTPS, CDN                                  │    │
│  └─────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      Railway                                 │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              FastAPI (Backend)                       │    │
│  │  - Docker 컨테이너                                   │    │
│  │  - 자동 스케일링                                     │    │
│  │  - 환경 변수 관리                                    │    │
│  └─────────────────────────────────────────────────────┘    │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Celery Worker                           │    │
│  │  - 비동기 작업 처리                                  │    │
│  │  - 예약/정기 발송                                    │    │
│  └─────────────────────────────────────────────────────┘    │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              Upstash Redis                           │    │
│  │  - Celery Broker                                    │    │
│  │  - 캐싱                                             │    │
│  └─────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      Supabase                                │
│  - PostgreSQL Database                                       │
│  - Auth (인증)                                               │
│  - Storage (파일)                                            │
│  - Realtime (실시간)                                         │
└─────────────────────────────────────────────────────────────┘
```

### 6.2 데이터베이스 스키마

```sql
-- 사업자 (Merchant)
CREATE TABLE merchants (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  business_name VARCHAR(255) NOT NULL,
  business_number VARCHAR(20) UNIQUE NOT NULL,
  representative_name VARCHAR(100) NOT NULL,
  phone VARCHAR(20) NOT NULL,
  address TEXT,
  bank_code VARCHAR(10),
  bank_account VARCHAR(50),
  bank_holder VARCHAR(100),
  status VARCHAR(20) DEFAULT 'PENDING', -- PENDING, ACTIVE, SUSPENDED
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- 고객 (Customer)
CREATE TABLE customers (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  merchant_id UUID REFERENCES merchants(id),
  name VARCHAR(100) NOT NULL,
  phone VARCHAR(20) NOT NULL,
  email VARCHAR(255),
  memo TEXT,
  tags TEXT[], -- 태그 배열
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),
  UNIQUE(merchant_id, phone)
);

-- 청구서 (Bill)
CREATE TABLE bills (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  merchant_id UUID REFERENCES merchants(id),
  customer_id UUID REFERENCES customers(id),
  bill_number VARCHAR(50) UNIQUE NOT NULL,

  -- 청구 정보
  amount INTEGER NOT NULL,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  items JSONB, -- 청구 항목

  -- 세금
  tax_type VARCHAR(20) DEFAULT 'TAX', -- TAX, TAX_FREE
  supply_amount INTEGER,
  tax_amount INTEGER,

  -- 발송 설정
  send_type VARCHAR(20) NOT NULL, -- IMMEDIATE, SCHEDULED, RECURRING
  send_channel VARCHAR(20) NOT NULL, -- ALIMTALK, SMS, BOTH
  scheduled_at TIMESTAMP,
  recurring_rule JSONB,

  -- 상태
  status VARCHAR(20) DEFAULT 'DRAFT',
  sent_at TIMESTAMP,
  viewed_at TIMESTAMP,
  paid_at TIMESTAMP,
  cancelled_at TIMESTAMP,
  expires_at TIMESTAMP,

  -- 메시지
  message TEXT,

  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- 결제 (Payment)
CREATE TABLE payments (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  bill_id UUID REFERENCES bills(id),
  merchant_id UUID REFERENCES merchants(id),

  -- 결제 정보
  amount INTEGER NOT NULL,
  method VARCHAR(50), -- CARD, KAKAO_PAY, NAVER_PAY, etc.
  pg_provider VARCHAR(50),
  pg_tid VARCHAR(100), -- PG 거래 ID

  -- 카드 정보 (마스킹)
  card_company VARCHAR(50),
  card_number VARCHAR(20), -- 마스킹된 번호
  installment INTEGER DEFAULT 0,

  -- 상태
  status VARCHAR(20) DEFAULT 'PENDING', -- PENDING, PAID, CANCELLED, FAILED
  paid_at TIMESTAMP,
  cancelled_at TIMESTAMP,
  cancel_reason TEXT,

  -- 정산
  settlement_amount INTEGER,
  settlement_at TIMESTAMP,

  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- 현금영수증 (CashReceipt)
CREATE TABLE cash_receipts (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  payment_id UUID REFERENCES payments(id),
  merchant_id UUID REFERENCES merchants(id),

  type VARCHAR(20) NOT NULL, -- INCOME, EXPENSE
  identity_type VARCHAR(20), -- PHONE, BUSINESS_NUMBER, CARD
  identity_number VARCHAR(50),
  amount INTEGER NOT NULL,

  approval_number VARCHAR(50),
  issued_at TIMESTAMP,
  cancelled_at TIMESTAMP,

  created_at TIMESTAMP DEFAULT NOW()
);

-- 알림 로그 (NotificationLog)
CREATE TABLE notification_logs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  bill_id UUID REFERENCES bills(id),

  channel VARCHAR(20) NOT NULL, -- ALIMTALK, SMS
  recipient VARCHAR(20) NOT NULL,
  status VARCHAR(20), -- SENT, DELIVERED, FAILED

  sent_at TIMESTAMP,
  delivered_at TIMESTAMP,
  error_message TEXT,

  created_at TIMESTAMP DEFAULT NOW()
);

-- 인덱스
CREATE INDEX idx_bills_merchant_id ON bills(merchant_id);
CREATE INDEX idx_bills_status ON bills(status);
CREATE INDEX idx_bills_created_at ON bills(created_at);
CREATE INDEX idx_payments_merchant_id ON payments(merchant_id);
CREATE INDEX idx_payments_status ON payments(status);
CREATE INDEX idx_customers_merchant_id ON customers(merchant_id);
```

---

## 7. UI/UX 설계

### 7.1 주요 화면 목록

#### 사업자 웹 (관리자)

| 화면 | 설명 |
|------|------|
| 로그인/회원가입 | 이메일/소셜 로그인, 사업자 인증 |
| 대시보드 | 오늘/이번달 매출, 미수금, 최근 결제 |
| 청구서 목록 | 청구서 목록 조회, 필터, 검색 |
| 청구서 작성 | 단건/대량 청구서 작성 |
| 고객 관리 | 고객 목록, 등록, 상세 |
| 매출/정산 | 매출 차트, 정산 내역, 보고서 |
| 현금영수증 | 발급 내역, 수동 발급 |
| 설정 | 프로필, 정산 계좌, 알림 설정 |

#### 고객 결제 페이지

| 화면 | 설명 |
|------|------|
| 청구서 확인 | 청구 내용 확인 |
| 결제 수단 선택 | 카드/간편결제 선택 |
| 결제 완료 | 결제 완료 및 영수증 |

### 7.2 와이어프레임 (주요 화면)

#### 대시보드

```
┌──────────────────────────────────────────────────────────┐
│  [LetsPay 로고]                    [알림] [프로필]       │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  ┌────────────┐ ┌────────────┐ ┌────────────┐           │
│  │ 오늘 매출  │ │ 이번달 매출 │ │  미수금    │           │
│  │ ₩1,250,000 │ │ ₩15,800,000│ │ ₩2,300,000 │           │
│  │ +12% ▲    │ │ +8% ▲     │ │ 23건       │           │
│  └────────────┘ └────────────┘ └────────────┘           │
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │              매출 추이 (최근 7일)                 │    │
│  │  ▁▃▅▇█▆▄                                        │    │
│  │  월 화 수 목 금 토 일                            │    │
│  └─────────────────────────────────────────────────┘    │
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │  최근 결제 내역                          [더보기] │    │
│  ├─────────────────────────────────────────────────┤    │
│  │  홍길동 | ₩150,000 | 1월 수업료 | 10분 전       │    │
│  │  김철수 | ₩200,000 | PT 10회권 | 1시간 전       │    │
│  │  이영희 | ₩80,000  | 교재비    | 3시간 전       │    │
│  └─────────────────────────────────────────────────┘    │
│                                                          │
│  [+ 청구서 발송]                                         │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

#### 청구서 작성

```
┌──────────────────────────────────────────────────────────┐
│  ← 청구서 작성                                           │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  발송 유형                                               │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐                 │
│  │ ○ 단건   │ │ ○ 대량   │ │ ○ 정기   │                 │
│  └──────────┘ └──────────┘ └──────────┘                 │
│                                                          │
│  ──────────────────────────────────────────────────     │
│                                                          │
│  고객 정보                                               │
│  ┌────────────────────────────────────┐                 │
│  │ 고객 선택 또는 직접 입력            ▼│                 │
│  └────────────────────────────────────┘                 │
│                                                          │
│  휴대폰 번호                                             │
│  ┌────────────────────────────────────┐                 │
│  │ 010-0000-0000                      │                 │
│  └────────────────────────────────────┘                 │
│                                                          │
│  ──────────────────────────────────────────────────     │
│                                                          │
│  청구 금액                                               │
│  ┌────────────────────────────────────┐                 │
│  │                          ₩ 150,000 │                 │
│  └────────────────────────────────────┘                 │
│                                                          │
│  청구 사유                                               │
│  ┌────────────────────────────────────┐                 │
│  │ 1월 수업료                         │                 │
│  └────────────────────────────────────┘                 │
│                                                          │
│  세금 유형   ○ 과세  ○ 면세                             │
│                                                          │
│  안내 메시지 (선택)                                      │
│  ┌────────────────────────────────────┐                 │
│  │                                    │                 │
│  └────────────────────────────────────┘                 │
│                                                          │
│  발송 시점   ○ 즉시 발송  ○ 예약 발송                   │
│                                                          │
│  ┌────────────────────────────────────────────────┐     │
│  │              청구서 발송하기                    │     │
│  └────────────────────────────────────────────────┘     │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

#### 고객 결제 페이지 (모바일)

```
┌─────────────────────────┐
│                         │
│    [사업자 로고/이름]    │
│    ABC 영어학원         │
│                         │
├─────────────────────────┤
│                         │
│    청구 금액            │
│    ₩150,000            │
│                         │
│    ─────────────────    │
│                         │
│    청구 내용            │
│    1월 수업료           │
│                         │
│    ─────────────────    │
│                         │
│    안내 메시지          │
│    2월 수업은 2/3부터   │
│    시작됩니다.          │
│                         │
├─────────────────────────┤
│                         │
│    결제 수단 선택       │
│                         │
│  ┌─────────────────┐    │
│  │   💳 카드 결제   │    │
│  └─────────────────┘    │
│                         │
│  ┌─────────────────┐    │
│  │  카카오페이     │    │
│  └─────────────────┘    │
│                         │
│  ┌─────────────────┐    │
│  │  네이버페이     │    │
│  └─────────────────┘    │
│                         │
│  ┌─────────────────┐    │
│  │   토스페이      │    │
│  └─────────────────┘    │
│                         │
│  [  자동결제 등록  ]     │
│                         │
└─────────────────────────┘
```

### 7.3 디자인 시스템

| 요소 | 값 |
|------|-----|
| Primary Color | #2563EB (Blue) |
| Secondary Color | #10B981 (Green) |
| Error Color | #EF4444 (Red) |
| Background | #F9FAFB |
| Text Primary | #111827 |
| Text Secondary | #6B7280 |
| Font Family | Pretendard, -apple-system |
| Border Radius | 8px (기본), 12px (카드) |

---

## 8. 개발 로드맵

### Phase 1: MVP (8주)

| 주차 | 마일스톤 | 주요 작업 |
|------|----------|----------|
| 1-2 | 프로젝트 셋업 | 개발 환경, DB 스키마, 인증 |
| 3-4 | 청구서 기능 | 청구서 CRUD, 단건 발송 |
| 5-6 | 결제 연동 | PG 연동, 결제 페이지 |
| 7-8 | 관리 기능 | 대시보드, 수납 관리, 테스트 |

**MVP 범위:**
- 회원가입/로그인
- 사업자 인증
- 단건 청구서 발송 (알림톡/SMS)
- 카드 결제 + 주요 간편결제
- 기본 대시보드
- 수납 현황

### Phase 2: 기능 확장 (6주)

| 주차 | 마일스톤 | 주요 작업 |
|------|----------|----------|
| 9-10 | 발송 고도화 | 대량 발송, 예약 발송, 정기 발송 |
| 11-12 | 고객 관리 | 고객 목록, 그룹, 엑셀 가져오기 |
| 13-14 | 보고서 | 매출 보고서, 현금영수증 |

### Phase 3: 고도화 (4주)

| 주차 | 마일스톤 | 주요 작업 |
|------|----------|----------|
| 15-16 | 자동화 | 자동결제, 정기 청구 |
| 17-18 | 확장 | 모바일 앱, 오프라인 단말기 |

---

## 9. 리스크 및 대응 방안

| 리스크 | 영향도 | 대응 방안 |
|--------|--------|----------|
| PG사 연동 지연 | 높음 | 조기 계약, 테스트 환경 확보 |
| 알림톡 발송 제한 | 중간 | SMS 대체 발송, 발송량 모니터링 |
| 개인정보 유출 | 높음 | 암호화, 접근 제어, 보안 감사 |
| 서비스 장애 | 높음 | 모니터링, 자동 복구, DR 구성 |
| 사용자 이탈 | 중간 | UX 개선, 온보딩 최적화 |

---

## 10. 성공 지표

### 10.1 제품 지표

| 지표 | 정의 | 목표 |
|------|------|------|
| 가입 전환율 | 방문자 → 가입 | 10% |
| 활성화율 | 가입 → 첫 청구서 발송 | 50% |
| 리텐션 (D30) | 30일 후 재사용 | 40% |
| 결제 성공률 | 청구서 발송 → 결제 | 70% |

### 10.2 비즈니스 지표

| 지표 | 정의 | 목표 (1년) |
|------|------|-----------|
| 가입자 수 | 누적 사업자 | 10,000명 |
| MAU | 월간 활성 사용자 | 5,000명 |
| 월 거래액 | 결제 처리액 | 50억원 |
| 매출 | 수수료 수익 | 5억원/년 |

---

## 11. 용어 정의

| 용어 | 정의 |
|------|------|
| 사업자 (Merchant) | LetsPay를 사용하여 청구서를 발송하는 사업자 |
| 고객 (Customer) | 청구서를 받고 결제하는 최종 사용자 |
| 청구서 (Bill) | 사업자가 고객에게 발송하는 결제 요청서 |
| 수납 | 고객이 청구서에 대해 결제를 완료한 상태 |
| 미수금 | 발송했으나 아직 결제되지 않은 청구 금액 |
| PG (Payment Gateway) | 결제 처리를 중개하는 서비스 |
| 알림톡 | 카카오톡으로 발송되는 비즈니스 메시지 |

---

## 12. 참고 자료

### 경쟁사 분석
- [경쟁사 분석 - 결제선생](./경쟁사분석_결제선생.md)

### 기술 문서
- [Vite 공식 문서](https://vitejs.dev)
- [React 공식 문서](https://react.dev)
- [FastAPI 공식 문서](https://fastapi.tiangolo.com)
- [Supabase 공식 문서](https://supabase.com/docs)
- [shadcn/ui 공식 문서](https://ui.shadcn.com)
- [TanStack Query 문서](https://tanstack.com/query)
- [Zustand 문서](https://zustand-demo.pmnd.rs)

### 외부 서비스 API
- [토스페이먼츠 API 문서](https://docs.tosspayments.com)
- [솔라피(Solapi) API 문서](https://docs.solapi.com)
- [공공데이터포털 - 사업자등록정보 진위확인](https://www.data.go.kr)

### 배포 플랫폼
- [Vercel 문서](https://vercel.com/docs)
- [Railway 문서](https://docs.railway.app)

---

