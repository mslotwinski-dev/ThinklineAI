import {
  IsString,
  IsInt,
  IsArray,
  Min,
  Max,
  ArrayNotEmpty,
  IsLocale,
  IsOptional,
} from 'class-validator'

export class GenerateDto {
  @IsString()
  language: string

  @IsInt()
  @Min(0)
  @Max(2)
  level: number

  @IsArray()
  @ArrayNotEmpty()
  @IsString({ each: true })
  tags: string[]

  @IsString()
  @IsLocale()
  locale: string

  @IsInt()
  @Min(0)
  @Max(10)
  topic: number

  @IsArray()
  @ArrayNotEmpty()
  @IsString({ each: true })
  @IsOptional()
  previous_projects?: string[]
}
