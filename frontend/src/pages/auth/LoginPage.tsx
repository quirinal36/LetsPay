import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { z } from 'zod'
import { Link, useNavigate } from 'react-router-dom'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'
import { useAuthStore } from '@/stores/authStore'

const loginSchema = z.object({
  email: z.string().email('올바른 이메일을 입력하세요'),
  password: z.string().min(1, '비밀번호를 입력하세요'),
})

type LoginFormData = z.infer<typeof loginSchema>

export default function LoginPage() {
  const navigate = useNavigate()
  const { login, loginWithGoogle, isLoading, error, clearError } = useAuthStore()

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<LoginFormData>({
    resolver: zodResolver(loginSchema),
  })

  const onSubmit = async (data: LoginFormData) => {
    clearError()
    await login(data.email, data.password)
    if (!error) {
      navigate('/dashboard')
    }
  }

  return (
    <div className="min-h-screen bg-background flex items-center justify-center p-4">
      <Card className="w-full max-w-md">
        <CardHeader className="text-center">
          <CardTitle className="text-2xl font-bold text-primary">로그인</CardTitle>
          <p className="text-muted-foreground text-sm">LetsPay에 오신 것을 환영합니다</p>
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
              <Input
                type="password"
                placeholder="비밀번호"
                {...register('password')}
                className={errors.password ? 'border-red-500' : ''}
              />
              {errors.password && (
                <p className="text-red-500 text-xs">{errors.password.message}</p>
              )}
            </div>

            <div className="flex justify-end">
              <Link to="/auth/forgot-password" className="text-sm text-primary hover:underline">
                비밀번호를 잊으셨나요?
              </Link>
            </div>

            <Button type="submit" className="w-full" disabled={isLoading}>
              {isLoading ? '로그인 중...' : '로그인'}
            </Button>

            <div className="relative my-4">
              <div className="absolute inset-0 flex items-center">
                <div className="w-full border-t border-gray-200" />
              </div>
              <div className="relative flex justify-center text-sm">
                <span className="bg-white px-2 text-gray-500">또는</span>
              </div>
            </div>

            <Button
              type="button"
              variant="outline"
              className="w-full"
              onClick={() => loginWithGoogle()}
              disabled={isLoading}
            >
              Google로 로그인
            </Button>

            <p className="text-center text-sm text-gray-600">
              계정이 없으신가요?{' '}
              <Link to="/auth/signup" className="text-primary hover:underline">
                회원가입
              </Link>
            </p>
          </form>
        </CardContent>
      </Card>
    </div>
  )
}
