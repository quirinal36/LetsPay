import { useState } from 'react'
import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { z } from 'zod'
import { Link, useNavigate } from 'react-router-dom'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'
import { useAuthStore } from '@/stores/authStore'

const signupSchema = z.object({
  email: z.string().email('올바른 이메일을 입력하세요'),
  password: z
    .string()
    .min(8, '비밀번호는 8자 이상이어야 합니다')
    .regex(/[A-Z]/, '대문자를 포함해야 합니다')
    .regex(/[a-z]/, '소문자를 포함해야 합니다')
    .regex(/[0-9]/, '숫자를 포함해야 합니다'),
  confirmPassword: z.string(),
  phone: z
    .string()
    .regex(/^01[0-9]-?[0-9]{3,4}-?[0-9]{4}$/, '올바른 휴대폰 번호를 입력하세요'),
  businessName: z.string().min(1, '사업자명을 입력하세요'),
  agreeTerms: z.boolean().refine((val) => val === true, {
    message: '이용약관에 동의해주세요',
  }),
}).refine((data) => data.password === data.confirmPassword, {
  message: '비밀번호가 일치하지 않습니다',
  path: ['confirmPassword'],
})

type SignupFormData = z.infer<typeof signupSchema>

export default function SignupPage() {
  const navigate = useNavigate()
  const { registerWithBusinessInfo, isLoading, error, clearError } = useAuthStore()
  const [showPassword, setShowPassword] = useState(false)

  const {
    register,
    handleSubmit,
    formState: { errors },
    watch,
  } = useForm<SignupFormData>({
    resolver: zodResolver(signupSchema),
    defaultValues: {
      agreeTerms: false,
    },
  })

  const password = watch('password', '')

  const getPasswordStrength = (pwd: string): { level: number; text: string; color: string } => {
    let score = 0
    if (pwd.length >= 8) score++
    if (/[A-Z]/.test(pwd)) score++
    if (/[a-z]/.test(pwd)) score++
    if (/[0-9]/.test(pwd)) score++
    if (/[^A-Za-z0-9]/.test(pwd)) score++

    if (score <= 2) return { level: score, text: '약함', color: 'bg-red-500' }
    if (score <= 3) return { level: score, text: '보통', color: 'bg-yellow-500' }
    return { level: score, text: '강함', color: 'bg-green-500' }
  }

  const passwordStrength = getPasswordStrength(password)

  const onSubmit = async (data: SignupFormData) => {
    clearError()
    const success = await registerWithBusinessInfo(data.email, data.password, data.phone, data.businessName)
    if (success) {
      navigate('/')
    }
  }

  return (
    <div className="min-h-screen bg-background flex items-center justify-center p-4">
      <Card className="w-full max-w-md">
        <CardHeader className="text-center">
          <CardTitle className="text-2xl font-bold text-primary">회원가입</CardTitle>
          <p className="text-muted-foreground text-sm">LetsPay 계정을 생성하세요</p>
        </CardHeader>
        <CardContent>
          <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
            {error && (
              <div className="p-3 bg-red-50 border border-red-200 rounded-md text-red-600 text-sm">
                {error}
              </div>
            )}

            <div className="space-y-2">
              <label className="text-sm font-medium">이메일</label>
              <Input
                type="email"
                placeholder="email@example.com"
                {...register('email')}
                className={errors.email ? 'border-red-500' : ''}
              />
              {errors.email && (
                <p className="text-red-500 text-xs">{errors.email.message}</p>
              )}
            </div>

            <div className="space-y-2">
              <label className="text-sm font-medium">비밀번호</label>
              <div className="relative">
                <Input
                  type={showPassword ? 'text' : 'password'}
                  placeholder="8자 이상, 대/소문자, 숫자 포함"
                  {...register('password')}
                  className={errors.password ? 'border-red-500' : ''}
                />
                <button
                  type="button"
                  onClick={() => setShowPassword(!showPassword)}
                  className="absolute right-3 top-1/2 -translate-y-1/2 text-gray-500 text-sm"
                >
                  {showPassword ? '숨김' : '표시'}
                </button>
              </div>
              {password && (
                <div className="flex items-center gap-2">
                  <div className="flex-1 h-1 bg-gray-200 rounded">
                    <div
                      className={`h-full rounded ${passwordStrength.color}`}
                      style={{ width: `${(passwordStrength.level / 5) * 100}%` }}
                    />
                  </div>
                  <span className="text-xs text-gray-500">{passwordStrength.text}</span>
                </div>
              )}
              {errors.password && (
                <p className="text-red-500 text-xs">{errors.password.message}</p>
              )}
            </div>

            <div className="space-y-2">
              <label className="text-sm font-medium">비밀번호 확인</label>
              <Input
                type="password"
                placeholder="비밀번호를 다시 입력하세요"
                {...register('confirmPassword')}
                className={errors.confirmPassword ? 'border-red-500' : ''}
              />
              {errors.confirmPassword && (
                <p className="text-red-500 text-xs">{errors.confirmPassword.message}</p>
              )}
            </div>

            <div className="space-y-2">
              <label className="text-sm font-medium">휴대폰 번호</label>
              <Input
                type="tel"
                placeholder="010-1234-5678"
                {...register('phone')}
                className={errors.phone ? 'border-red-500' : ''}
              />
              {errors.phone && (
                <p className="text-red-500 text-xs">{errors.phone.message}</p>
              )}
            </div>

            <div className="space-y-2">
              <label className="text-sm font-medium">사업자명</label>
              <Input
                type="text"
                placeholder="사업자/상호명"
                {...register('businessName')}
                className={errors.businessName ? 'border-red-500' : ''}
              />
              {errors.businessName && (
                <p className="text-red-500 text-xs">{errors.businessName.message}</p>
              )}
            </div>

            <div className="flex items-start gap-2">
              <input
                type="checkbox"
                id="agreeTerms"
                {...register('agreeTerms')}
                className="mt-1"
              />
              <label htmlFor="agreeTerms" className="text-sm text-gray-600">
                <span className="text-primary underline cursor-pointer">이용약관</span> 및{' '}
                <span className="text-primary underline cursor-pointer">개인정보처리방침</span>에
                동의합니다
              </label>
            </div>
            {errors.agreeTerms && (
              <p className="text-red-500 text-xs">{errors.agreeTerms.message}</p>
            )}

            <Button type="submit" className="w-full" disabled={isLoading}>
              {isLoading ? '처리중...' : '회원가입'}
            </Button>

            <p className="text-center text-sm text-gray-600">
              이미 계정이 있으신가요?{' '}
              <Link to="/auth/login" className="text-primary hover:underline">
                로그인
              </Link>
            </p>
          </form>
        </CardContent>
      </Card>
    </div>
  )
}
