# LetsPay Project Setup Specification

## Overview

이 문서는 LetsPay 프로젝트 초기 설정 (Issues #1, #2, #3)을 위한 기술 사양서입니다.

---

## 1. Requirements Analysis

### 1.1 Functional Requirements

| Category | Requirement |
|----------|-------------|
| Frontend | React 18 + Vite + TypeScript 프로젝트 구조 생성 |
| Frontend | Tailwind CSS + shadcn/ui 설정 |
| Frontend | Zustand + TanStack Query 상태 관리 설정 |
| Frontend | React Router v6 라우팅 설정 |
| Backend | FastAPI + Python 3.11+ 프로젝트 구조 생성 |
| Backend | SQLAlchemy 2.0 + Pydantic v2 설정 |
| Backend | API 버전관리 (/api/v1/) 구조 |
| Database | Supabase PostgreSQL 6개 핵심 테이블 생성 |
| Database | Row Level Security (RLS) 정책 설정 |
| Auth | Supabase Auth 이메일/비밀번호 인증 |
| Auth | 소셜 로그인 (Google 우선, Kakao/Naver 후순위) |

### 1.2 Non-Functional Requirements

| Category | Requirement |
|----------|-------------|
| DX | TypeScript strict mode 활성화 |
| DX | ESLint + Prettier (FE), Ruff (BE) 린팅 설정 |
| DX | Hot Module Replacement (HMR) 지원 |
| Security | 환경변수 기반 설정 관리 |
| Security | CORS 설정 (localhost 개발환경) |
| Performance | Vite 빌드 최적화 |

### 1.3 Out of Scope (Phase 1 Setup)

- Celery/ARQ 태스크 큐 (Phase 2)
- Supabase Storage 버킷 설정
- Supabase Realtime 구독
- 전체 shadcn/ui 컴포넌트 설치 (필요시 추가)
- 다중 소셜 로그인 (Google만 우선 설정)

---

## 2. Tech Stack

### 2.1 Frontend

| Technology | Version | Purpose |
|------------|---------|---------|
| Vite | ^5.x | Build tool |
| React | ^18.x | UI framework |
| TypeScript | ^5.x | Language |
| Tailwind CSS | ^3.x | Styling |
| shadcn/ui | latest | Component library |
| Zustand | ^4.x | Global state |
| TanStack Query | ^5.x | Server state |
| React Hook Form | ^7.x | Forms |
| Zod | ^3.x | Validation |
| React Router | ^6.x | Routing |
| pnpm | ^8.x | Package manager |

### 2.2 Backend

| Technology | Version | Purpose |
|------------|---------|---------|
| FastAPI | ^0.110.x | Framework |
| Python | ^3.11 | Language |
| SQLAlchemy | ^2.0 | ORM |
| Pydantic | ^2.x | Validation |
| Poetry | latest | Package manager |
| Ruff | latest | Linting |

### 2.3 Infrastructure

| Service | Purpose |
|---------|---------|
| Supabase | PostgreSQL + Auth |
| Vercel | Frontend hosting |
| Railway | Backend hosting |

---

## 3. Project Structure

### 3.1 Root Structure

```
letspay/
├── frontend/           # React + Vite
├── backend/            # FastAPI
├── docs/               # Documentation
├── .github/            # CI/CD workflows
├── PRD.md
└── README.md
```

### 3.2 Frontend Structure

```
frontend/
├── src/
│   ├── components/
│   │   ├── ui/         # shadcn/ui
│   │   ├── layout/     # Header, Sidebar, etc.
│   │   └── common/     # Shared components
│   ├── pages/          # Route pages
│   ├── hooks/          # Custom hooks
│   ├── stores/         # Zustand stores
│   ├── services/       # API services
│   ├── types/          # TypeScript types
│   ├── utils/          # Utilities
│   ├── lib/            # Third-party setup
│   └── styles/         # Global styles
├── package.json
├── vite.config.ts
├── tailwind.config.ts
└── tsconfig.json
```

### 3.3 Backend Structure

```
backend/
├── app/
│   ├── api/
│   │   └── v1/         # API version 1
│   ├── core/           # Config, security
│   ├── models/         # SQLAlchemy models
│   ├── schemas/        # Pydantic schemas
│   ├── services/       # Business logic
│   ├── repositories/   # Data access
│   └── utils/          # Utilities
├── tests/
├── pyproject.toml
└── Dockerfile
```

---

## 4. Database Schema

### 4.1 Core Tables

1. **merchants** - 사업자 정보
2. **customers** - 고객 정보
3. **bills** - 청구서
4. **payments** - 결제
5. **cash_receipts** - 현금영수증
6. **notification_logs** - 알림 로그

### 4.2 Auth Integration

- Supabase Auth `auth.users` 테이블과 `merchants` 테이블 연동
- `merchants.id` = `auth.users.id` (동일 UUID 사용)
- RLS 정책으로 merchant별 데이터 격리

---

## 5. Environment Variables

### 5.1 Frontend (.env.local)

```bash
VITE_APP_NAME=LetsPay
VITE_API_URL=http://localhost:8000/api/v1
VITE_SUPABASE_URL=https://xxx.supabase.co
VITE_SUPABASE_ANON_KEY=xxx
```

### 5.2 Backend (.env)

```bash
ENVIRONMENT=development
DATABASE_URL=postgresql+asyncpg://...
SUPABASE_URL=https://xxx.supabase.co
SUPABASE_SERVICE_ROLE_KEY=xxx
SECRET_KEY=xxx
CORS_ORIGINS=["http://localhost:5173"]
```

---

## 6. Acceptance Criteria

### Issue #1: 프로젝트 초기 구조 설정

- [ ] `pnpm dev` 실행시 localhost:5173에서 프론트엔드 동작
- [ ] `uvicorn app.main:app` 실행시 localhost:8000/docs 접근 가능
- [ ] TypeScript 컴파일 에러 없음
- [ ] Python 타입체크 (mypy) 통과

### Issue #2: Supabase 데이터베이스 스키마 설정

- [ ] 6개 핵심 테이블 생성 완료
- [ ] RLS 정책 활성화
- [ ] 인덱스 생성 완료

### Issue #3: Supabase Auth 설정

- [ ] 이메일/비밀번호 회원가입 동작
- [ ] 로그인 후 JWT 토큰 발급
- [ ] FastAPI에서 JWT 검증 동작
- [ ] Google 소셜 로그인 동작

---

**EXPANSION_COMPLETE**
