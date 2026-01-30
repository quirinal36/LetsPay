import { Link } from 'react-router-dom'
import { Button } from '@/components/ui/button'
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'

export default function Home() {
  return (
    <div className="min-h-screen bg-background flex items-center justify-center p-4">
      <Card className="w-full max-w-md">
        <CardHeader className="text-center">
          <CardTitle className="text-2xl font-bold text-primary">LetsPay</CardTitle>
          <p className="text-muted-foreground">모바일 청구서 발송 및 수납 관리 플랫폼</p>
        </CardHeader>
        <CardContent className="space-y-4">
          <Link to="/auth/login" className="block">
            <Button className="w-full">로그인</Button>
          </Link>
          <Link to="/auth/signup" className="block">
            <Button variant="outline" className="w-full">회원가입</Button>
          </Link>
        </CardContent>
      </Card>
    </div>
  )
}
