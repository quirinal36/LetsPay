# Supabase Auth Setup Guide

## 1. Supabase 프로젝트 생성

1. [Supabase Dashboard](https://supabase.com/dashboard) 접속
2. "New Project" 클릭
3. 프로젝트 정보 입력:
   - Name: `letspay`
   - Database Password: 강력한 비밀번호 설정
   - Region: `Northeast Asia (Seoul)` 선택

## 2. 데이터베이스 스키마 적용

SQL Editor에서 순서대로 실행:

1. `docs/database/001_initial_schema.sql` - 테이블 생성
2. `docs/database/002_rls_policies.sql` - RLS 정책
3. `docs/database/003_auth_trigger.sql` - 회원가입 트리거

## 3. Email/Password 인증 설정

1. Authentication > Providers 이동
2. Email provider 설정:
   - Enable Email provider: ✓
   - Confirm email: ✓ (이메일 확인 필수)
   - Secure email change: ✓

## 4. Google OAuth 설정

### Google Cloud Console 설정

1. [Google Cloud Console](https://console.cloud.google.com) 접속
2. 새 프로젝트 생성 또는 기존 프로젝트 선택
3. APIs & Services > Credentials 이동
4. "Create Credentials" > "OAuth client ID" 선택
5. Application type: "Web application"
6. Authorized redirect URIs 추가:
   ```
   https://<project-ref>.supabase.co/auth/v1/callback
   ```
7. Client ID와 Client Secret 복사

### Supabase 설정

1. Authentication > Providers > Google
2. Enable Google: ✓
3. Client ID 입력
4. Client Secret 입력
5. Save 클릭

## 5. 환경 변수 설정

### API Keys 확인

Settings > API에서 확인:

- `Project URL`: VITE_SUPABASE_URL / SUPABASE_URL
- `anon public`: VITE_SUPABASE_ANON_KEY / SUPABASE_ANON_KEY
- `service_role`: SUPABASE_SERVICE_ROLE_KEY (백엔드만)

### JWT Secret 확인

Settings > API > JWT Settings:
- `JWT Secret`: SUPABASE_JWT_SECRET

### Frontend `.env.local`

```bash
VITE_SUPABASE_URL=https://xxx.supabase.co
VITE_SUPABASE_ANON_KEY=eyJhbGc...
```

### Backend `.env`

```bash
SUPABASE_URL=https://xxx.supabase.co
SUPABASE_ANON_KEY=eyJhbGc...
SUPABASE_SERVICE_ROLE_KEY=eyJhbGc...
SUPABASE_JWT_SECRET=your-jwt-secret
```

## 6. 인증 플로우

### 회원가입

```typescript
const { data, error } = await supabase.auth.signUp({
  email: 'user@example.com',
  password: 'password123'
})
```

회원가입 시 자동으로:
1. `auth.users` 테이블에 사용자 생성
2. `003_auth_trigger.sql`에 의해 `merchants` 테이블에 레코드 생성
3. 이메일 확인 링크 발송

### 로그인

```typescript
const { data, error } = await supabase.auth.signInWithPassword({
  email: 'user@example.com',
  password: 'password123'
})
```

### Google 로그인

```typescript
const { data, error } = await supabase.auth.signInWithOAuth({
  provider: 'google',
  options: {
    redirectTo: `${window.location.origin}/auth/callback`
  }
})
```

### 토큰 검증 (FastAPI)

```python
from app.core.security import verify_supabase_token

@router.get("/protected")
async def protected_route(token: TokenData = Depends(verify_supabase_token)):
    return {"user_id": token.sub}
```

## 7. 테스트

### Frontend 테스트

1. `pnpm dev` 실행
2. http://localhost:5173 접속
3. 회원가입 테스트
4. 이메일 확인
5. 로그인 테스트

### Backend 테스트

1. `poetry run uvicorn app.main:app --reload` 실행
2. http://localhost:8000/docs 접속
3. Authorize 버튼 클릭
4. Supabase에서 받은 JWT 토큰 입력
5. `/api/v1/auth/me` 엔드포인트 테스트

## 8. 추가 설정 (선택)

### Kakao OAuth

1. [Kakao Developers](https://developers.kakao.com) 접속
2. 애플리케이션 생성
3. REST API 키 복사
4. Supabase > Authentication > Providers > Kakao에 설정

### Naver OAuth

1. [Naver Developers](https://developers.naver.com) 접속
2. 애플리케이션 등록
3. Client ID/Secret 복사
4. Supabase > Authentication > Providers > Custom에 설정
